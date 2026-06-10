# Install for other agents

`README.md` covers QoderWork, Claude Code, and the universal install. This page collects the platform-specific recipes that used to live in the README.

The skill itself is self-contained markdown. Pick whichever recipe matches your agent.

---

## OpenAI Codex CLI

Codex discovers instructions via `AGENTS.md` files. Two approaches:

**A — Symlink as a skill folder (recommended):**
```bash
ln -s $(pwd)/quant-guru-desk ~/.codex/skills/quant-guru-desk
```

**B — Reference in your global AGENTS.md:**
```bash
echo '## Skills
Read ~/.codex/skills/quant-guru-desk/SKILL.md for the quant-guru-desk investment agent collection.' >> ~/.codex/AGENTS.md
```

Codex follows the reference chain from SKILL.md → guru sub-files → shared resources.

---

## Cursor IDE

Cursor uses `.cursor/rules/` (`.mdc` files with YAML frontmatter).

**A — Global rule:**

`~/.cursor/rules/quant-guru-desk.mdc`:
```markdown
---
description: "Quant Guru Desk — summon investing-guru agents for stock analysis"
globs: "*"
alwaysApply: false
---

When the user asks for stock analysis, guru analysis, or mentions Serenity / Kindig / Cathie / Buffett / Dalio / Minervini / 会诊 / 投资竞赛, read and follow:
~/.cursor/skills/quant-guru-desk/SKILL.md
```

Then clone:
```bash
git clone https://github.com/chuehjen/quant-guru-desk.git ~/.cursor/skills/quant-guru-desk
```

**B — Project-level:**
```bash
cp -R quant-guru-desk .cursor/skills/quant-guru-desk
```
Add a rule file at `.cursor/rules/quant-guru-desk.mdc` referencing `.cursor/skills/quant-guru-desk/SKILL.md`.

---

## Windsurf (Codeium)

**A — Global rule (recommended):** Settings → Cascade → Global Rules:
```
When the user asks for stock analysis or mentions Serenity / Kindig / Cathie / Buffett / Dalio / Minervini / 会诊 / 投资竞赛, read and follow:
~/.windsurf/skills/quant-guru-desk/SKILL.md
```
Then:
```bash
git clone https://github.com/chuehjen/quant-guru-desk.git ~/.windsurf/skills/quant-guru-desk
```

**B — Project-level:** `.windsurf/rules/quant-guru-desk.md`:
```markdown
---
trigger: glob
globs: ["*"]
---

For investment analysis tasks, read .windsurf/skills/quant-guru-desk/SKILL.md and follow the guru methodology.
```

---

## Cline / Roo Code (VS Code)

```bash
git clone https://github.com/chuehjen/quant-guru-desk.git ~/Documents/Cline/Skills/quant-guru-desk

cat > ~/Documents/Cline/Rules/quant-guru-desk.md << 'EOF'
# Quant Guru Desk

When the user asks for stock analysis, guru analysis, or mentions
Serenity / Kindig / Cathie / Buffett / Dalio / Minervini / 会诊 / 投资竞赛 / 大神事务所:

Read and follow ~/Documents/Cline/Skills/quant-guru-desk/SKILL.md
EOF
```

Project-level alternative:
```bash
cp -R quant-guru-desk .clinerules/quant-guru-desk
```

---

## GitHub Copilot

Copilot reads `.github/copilot-instructions.md`:

```bash
cat >> .github/copilot-instructions.md << 'EOF'

## Investment Analysis (Quant Guru Desk)

For stock analysis and investment research tasks, reference the quant-guru-desk
skill at: ~/.github/skills/quant-guru-desk/SKILL.md

Routing: Buffett (value), Dalio (macro), Kindig (forward-revenue),
Cathie Wood (disruption), Serenity (supply chain), Minervini (timing).
Panel mode for multi-guru debate. Calls are graded by scripts/track_calls.py.
EOF

git clone https://github.com/chuehjen/quant-guru-desk.git ~/.github/skills/quant-guru-desk
```

> Copilot cannot read external files at runtime. The instructions above are context hints — for full functionality, paste key sections of `SKILL.md` into `copilot-instructions.md` or use Copilot Chat's `@workspace` with the skill folder in your project.

---

## Universal install (any agent that reads markdown)

```bash
git clone https://github.com/chuehjen/quant-guru-desk.git <agent-skills-path>/quant-guru-desk
```

Point your agent's system prompt or instruction file to `SKILL.md`. The skill is self-contained — `SKILL.md` references `gurus/*/SKILL.md` and `shared/*.md` via relative paths.

---

## Verifying install

After installing, ask the agent:

```
列出 quant-guru-desk 当前的大神花名册
```

You should get back the 6-guru roster (Buffett / Dalio / Kindig / Cathie / Serenity / Minervini). If only 3 show up, the agent loaded a stale copy — `git pull` and reload.

For Reflection-as-core to work, set the API key once:

```bash
export TWELVEDATA_API_KEY=your_free_key
scripts/track_calls.py summary
```
