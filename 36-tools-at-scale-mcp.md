# 🛡️ Mission 36 — Tools at Scale: MCP & Plugins

**🎯 Your job:** Scale your agent's toolset the way real agent platforms do — define tools as a protocol (MCP-style) so new capabilities plug in without rewriting the loop. Ties Track 3's tool loop to production extension.

**🧠 Why:** Hard-coded tools don't scale; a protocol does. This is the architectural leap from "my agent has 2 tools" to "my agent has a marketplace." You've seen HADA's tool surface — now you build the seam.

## 🛠️ Activity
- [ ] **🤖 Prompt to your AI coder:**
      > "In ~/ai-eng, write mcp_lite.py: define tools as JSON descriptors {name, description, input_schema, handler_ref} loaded from a tools/ dir at startup. The agent_loop discovers them dynamically (no imports in the loop). Add one example plugin (e.g. a 'time' tool) as a separate file. Print the discovered tool list."
- [ ] **Run it.** Confirm the loop picks up the plugin tool without code changes to the loop.
- [ ] **👀 What to watch for:** schema validation at the boundary — a malformed plugin must fail loud, not crash the agent mid-task.
- [ ] **✍️ Your move:** in `loot.md`, write one sentence: *"A tool protocol matters because ___."*

**🏆 Done when:** `mcp_lite.py` loads tools from a dir as JSON descriptors and the loop uses a plugin, and `loot.md` explains the protocol value.
