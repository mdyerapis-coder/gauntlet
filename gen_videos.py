#!/usr/bin/env python3
"""Generate the gauntlet's cinematic video breaks offline (no API/key).
Uses Pillow + imageio-ffmpeg (bundled ffmpeg). Style: violet/cyan arcane-tech
codex motion graphics. Outputs media/<name>.mp4 (WEBM-free, h264 mp4).
Run: uv run python gen_videos.py   (from the workbook dir)
"""
import os, math, random, imageio.v2 as imageio, numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "media")
os.makedirs(OUT, exist_ok=True)

W, H, FPS = 640, 360, 25
VIOLET = (140, 110, 255)
CYAN   = (86, 212, 255)
GOLD   = (255, 200, 110)
DARK   = (12, 16, 23)
DARK2  = (20, 16, 46)

random.seed(7)

def bg(t, fade=0.0):
    """radial dark gradient background, subtle pulse."""
    img = Image.new("RGB", (W, H), DARK)
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2
    r = int(80 + 14*math.sin(t*1.3))
    for i in range(6):
        rr = r - i*12
        if rr <= 0: continue
        col = (int(DARK2[0]*(1-i*0.08)), int(DARK2[1]*(1-i*0.08)), int(DARK2[2]*(1-i*0.08)))
        d.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], outline=col)
    if fade:
        ov = Image.new("RGB", (W,H), (0,0,0))
        img = Image.blend(img, ov, fade)
    return img

def glow_ellipse(d, cx, cy, r, color, a=1.0):
    g = Image.new("RGB", (W,H), (0,0,0))
    gd = ImageDraw.Draw(g)
    gd.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)
    g = g.filter(ImageFilter.GaussianBlur(12*a))
    return g

def composite(*imgs):
    base = imgs[0].copy()
    for im in imgs[1:]:
        base = Image.blend(base, im, 0.6)
    return base

def draw_ring(d, cx, cy, r, color, spin, dash=True):
    # draw a dashed/segmented ring rotated by spin
    for k in range(48):
        ang = spin + k*(2*math.pi/48)
        if dash and k % 3 == 0: continue
        x = cx + r*math.cos(ang); y = cy + r*math.sin(ang)
        d.ellipse([x-2, y-2, x+2, y+2], fill=color)

def draw_shield(d, cx, cy, s, color, lw=3):
    pts = [(cx, cy-s), (cx+s*0.7, cy-s*0.5), (cx+s*0.7, cy+s*0.2),
           (cx, cy+s*0.6), (cx-s*0.7, cy+s*0.2), (cx-s*0.7, cy-s*0.5)]
    d.line(pts+[pts[0]], fill=color, width=lw, joint="curve")

def draw_tower(d, cx, cy, s, color, blocks=4):
    for i in range(blocks):
        y = cy - s + i*(s*1.6/blocks)
        d.rectangle([cx-s*0.4, y, cx+s*0.4, y+s*0.3], outline=color, width=2)

def glyph_stream(n, t):
    """floating code glyphs drifting up."""
    out = Image.new("RGB", (W,H), (0,0,0))
    d = ImageDraw.Draw(out)
    for i in range(n):
        x = (i*53 + int(40*t)) % W
        y = (H + (i*37 - int(60*t)) % (H+30)) % (H+30) - 15
        ch = "01{}[]<>/\\|=+*"[i % 12]
        d.text((x, y), ch, fill=(random.choice([VIOLET,CYAN]))[:3])
    return out.filter(ImageFilter.GaussianBlur(1.2))

def clip(name, seconds, frame_fn):
    N = int(seconds*FPS)
    frames = []
    for i in range(N):
        t = i/FPS
        p = i/N
        img = frame_fn(t, p)
        img = img.filter(ImageFilter.GaussianBlur(0.4))
        frames.append(np.array(img))
    path = os.path.join(OUT, name)
    imageio.mimsave(path, frames, fps=FPS, codec="libx264", macro_block_size=1, quality=7)
    print(f"  {name}: {os.path.getsize(path)//1024} KB")

def fade_in(p): return max(0.0, 0.5 - p*3)
def fade_out(p): return max(0.0, (p-0.85)*6)

print("Generating gauntlet video breaks (offline)…")

def intro(t, p):
    img = bg(t, fade_in(p)+fade_out(p))
    g = glyph_stream(26, t*1.4)
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2
    draw_shield(d, cx, cy, 42, VIOLET, 4)
    draw_ring(d, cx, cy, 60, CYAN, t*1.5)
    draw_ring(d, cx, cy, 72, VIOLET, -t*1.0)
    gi = Image.blend(img, g, 0.5*math.sin(p*math.pi))
    return gi

def track(src_emblem, dst_emblem, n):
    def fn(t, p):
        img = bg(t, fade_in(p)+fade_out(p))
        d = ImageDraw.Draw(img)
        cx, cy = W//2, H//2
        # morph: src shrinks/left, dst grows/right
        a = p
        s1 = 40*(1-a)+8; x1 = cx-60*(a)
        s2 = 8+40*a;    x2 = cx+60*(a)
        if src_emblem=="shield": draw_shield(d, x1, cy, s1, VIOLET)
        else: draw_tower(d, x1, cy, s1, CYAN)
        if dst_emblem=="tower": draw_tower(d, x2, cy, s2, VIOLET)
        elif dst_emblem=="eye":
            d.ellipse([x2-14,x2-14,x2+14,x2+14], outline=CYAN, width=3)
            d.ellipse([x2-5,x2-5,x2+5,x2+5], fill=GOLD)
        elif dst_emblem=="server":
            d.rectangle([x2-22, cy-14, x2+22, cy+14], outline=VIOLET, width=3)
            draw_ring(d, x2, cy, 26, CYAN, t*2)
        draw_ring(d, cx, cy, 70, VIOLET, t)
        return img
    return fn

def finale(t, p):
    img = bg(t, fade_in(p)+fade_out(p))
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2
    # spiral of emblems
    for k in range(5):
        ang = t*1.5 + k*(2*math.pi/5)
        r = 30 + 22*math.sin(p*math.pi)
        x = cx + r*math.cos(ang); y = cy + r*math.sin(ang)
        col = [VIOLET,CYAN,GOLD,VIOLET,CYAN][k]
        draw_shield(d, x, y, 12, col, 2) if k%2==0 else draw_tower(d, x, y, 12, col)
    # central burst
    draw_ring(d, cx, cy, 20+20*p, GOLD, t*3)
    draw_ring(d, cx, cy, 40+40*p, CYAN, -t*2)
    return img

clip("intro.mp4", 5, intro)
clip("track1-2.mp4", 6, track("shield","tower",0))
clip("track2-3.mp4", 6, track("tower","eye",0))
clip("track3-4.mp4", 6, track("eye","server",0))
clip("finale.mp4", 7, finale)
print("Done.")
