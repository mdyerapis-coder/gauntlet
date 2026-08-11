#!/usr/bin/env python3
"""
gauntlet-terminal.py — local WebSocket-to-shell bridge for the Gauntlet's in-app terminal.

WHY: xterm.js in the browser can render a terminal, but browser JS can never spawn a real
shell process — that needs a server. This tiny stdlib-only WebSocket server spawns a real
pty running your shell per connection and streams it to the browser over a local WebSocket.

SECURITY: this gives ANY client that can reach this port a real, unauthenticated shell on
your machine. It binds to 127.0.0.1 only, on purpose — do not change that to 0.0.0.0 unless
you put real authentication in front of it first.

USAGE:
  python3 gauntlet-terminal.py            # serves ws://localhost:8842
  Open gauntlet.html, expand the ▶ Terminal panel on any mission — it connects automatically.

No external deps. Python 3.8+. Linux/macOS only (uses pty/termios, not available on Windows).
"""
import asyncio
import base64
import fcntl
import hashlib
import json
import os
import pty
import signal
import struct
import sys
import termios

PORT = 8842
WS_MAGIC = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
SHELL = os.environ.get("SHELL", "/bin/bash")


def ws_accept_key(key: str) -> str:
    return base64.b64encode(hashlib.sha1((key + WS_MAGIC).encode()).digest()).decode()


def make_frame(data: bytes, opcode: int = 0x2) -> bytes:
    """Server->client frames are never masked (per the WS spec)."""
    fin_op = 0x80 | opcode
    length = len(data)
    if length < 126:
        header = bytes([fin_op, length])
    elif length < (1 << 16):
        header = bytes([fin_op, 126]) + struct.pack(">H", length)
    else:
        header = bytes([fin_op, 127]) + struct.pack(">Q", length)
    return header + data


class WSFrameParser:
    """Incremental parser for client->server (always-masked) WS frames over a byte stream."""

    def __init__(self):
        self.buf = b""

    def feed(self, data: bytes):
        self.buf += data
        frames = []
        while True:
            frame, consumed = self._try_parse(self.buf)
            if frame is None:
                break
            frames.append(frame)
            self.buf = self.buf[consumed:]
        return frames

    def _try_parse(self, buf: bytes):
        if len(buf) < 2:
            return None, 0
        b0, b1 = buf[0], buf[1]
        opcode = b0 & 0x0F
        masked = bool(b1 & 0x80)
        length = b1 & 0x7F
        idx = 2
        if length == 126:
            if len(buf) < idx + 2:
                return None, 0
            length = struct.unpack(">H", buf[idx:idx + 2])[0]
            idx += 2
        elif length == 127:
            if len(buf) < idx + 8:
                return None, 0
            length = struct.unpack(">Q", buf[idx:idx + 8])[0]
            idx += 8
        mask_key = b""
        if masked:
            if len(buf) < idx + 4:
                return None, 0
            mask_key = buf[idx:idx + 4]
            idx += 4
        if len(buf) < idx + length:
            return None, 0
        payload = buf[idx:idx + length]
        if masked:
            payload = bytes(b ^ mask_key[i % 4] for i, b in enumerate(payload))
        idx += length
        return (opcode, payload), idx


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    peer = writer.get_extra_info("peername")
    try:
        # --- HTTP -> WebSocket upgrade handshake ---
        req = b""
        while b"\r\n\r\n" not in req:
            chunk = await reader.read(4096)
            if not chunk:
                writer.close()
                return
            req += chunk
        headers = req.decode(errors="replace")
        key = None
        for line in headers.split("\r\n"):
            if line.lower().startswith("sec-websocket-key:"):
                key = line.split(":", 1)[1].strip()
        if not key:
            writer.write(b"HTTP/1.1 400 Bad Request\r\n\r\n")
            await writer.drain()
            writer.close()
            return
        accept = ws_accept_key(key)
        resp = (
            "HTTP/1.1 101 Switching Protocols\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Accept: {accept}\r\n\r\n"
        )
        writer.write(resp.encode())
        await writer.drain()
        print(f"[gauntlet-terminal] client connected from {peer}, spawning {SHELL}")

        # --- spawn a real pty running the user's shell ---
        pid, fd = pty.fork()
        if pid == 0:
            signal.signal(signal.SIGCHLD, signal.SIG_DFL)
            os.execvp(SHELL, [SHELL, "-l"])
            os._exit(1)  # pragma: no cover — only reached if exec fails

        loop = asyncio.get_event_loop()
        parser = WSFrameParser()

        def on_pty_readable():
            try:
                data = os.read(fd, 65536)
            except OSError:
                data = b""
            if not data:
                try:
                    loop.remove_reader(fd)
                except Exception:
                    pass
                return
            writer.write(make_frame(data))
            asyncio.ensure_future(writer.drain())

        loop.add_reader(fd, on_pty_readable)

        try:
            while True:
                chunk = await reader.read(65536)
                if not chunk:
                    break
                for opcode, payload in parser.feed(chunk):
                    if opcode == 0x8:  # close frame
                        raise ConnectionResetError
                    elif opcode == 0x1:  # text frame: JSON control message (resize)
                        try:
                            msg = json.loads(payload.decode())
                            if msg.get("type") == "resize":
                                rows, cols = int(msg["rows"]), int(msg["cols"])
                                fcntl.ioctl(fd, termios.TIOCSWINSZ,
                                            struct.pack("HHHH", rows, cols, 0, 0))
                        except Exception:
                            pass
                    elif opcode == 0x2:  # binary frame: raw keystrokes -> pty stdin
                        os.write(fd, payload)
        except (ConnectionResetError, BrokenPipeError, OSError):
            pass
        finally:
            print(f"[gauntlet-terminal] client {peer} disconnected")
            try:
                loop.remove_reader(fd)
            except Exception:
                pass
            try:
                os.kill(pid, signal.SIGHUP)
            except Exception:
                pass
            try:
                os.close(fd)
            except Exception:
                pass
    finally:
        writer.close()


async def main(port: int):
    server = await asyncio.start_server(handle_client, "127.0.0.1", port)
    print(f"Gauntlet terminal bridge on ws://localhost:{port}  (127.0.0.1 only, real shell: {SHELL})")
    print("This gives anything that can reach this port a real shell on your machine. Ctrl+C to stop.")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    if sys.platform.startswith("win"):
        print("gauntlet-terminal.py needs a real pty (Linux/macOS) — not supported on Windows.")
        sys.exit(1)
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    try:
        asyncio.run(main(port))
    except KeyboardInterrupt:
        print("\nstopped.")
