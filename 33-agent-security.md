# 🛡️ Mission 33 — Agent Security: Sandbox & Permissions

**🎯 Your job:** Secure the agent you built in Track 3. Tools execute real code/functions — that's power and risk. Add a permission model + a sandbox boundary so a bad prompt can't wreck the host.

**🧠 Why:** HADA/Pantheon orchestrate untrusted-ish work. Agent security is the difference between a helpful tool and a remote-code-execution bug. You should design the guardrail, not discover the breach.

## 🛠️ Activity
- [ ] **🤖 Prompt to your AI coder:**
      > "In ~/ai-eng, write sandbox.py: wrap the agent_loop tool dispatch with (1) an allowlist of permitted tool names, (2) a per-tool timeout, (3) a confirmation gate for 'dangerous' tools (marked in tools.py), and (4) capture of stdout/stderr so tool output can't escape to the shell. Demonstrate blocking a disallowed tool call."
- [ ] **Run it** with a prompt that tries to call a non-allowlisted tool. Confirm it's blocked with a clear reason.
- [ ] **👀 What to watch for:** "dangerous" is a policy you define, not the model's guess. Make the list explicit and auditable.
- [ ] **✍️ Your move:** in `loot.md`, list 2 tools you'd mark dangerous and one sentence: *"A permission model fails if ___."*

**🏆 Done when:** `sandbox.py` enforces an allowlist + timeout + danger-gate, blocks a bad call, and `loot.md` names your dangerous tools.
