# Quant Guru Desk 🏛️

> A desk of distilled investing-guru AI agents. Summon any famous investor to analyze a stock, build a portfolio, or run a daily competition decision — in their authentic style. One project, many gurus.

**v2.0.0** · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)

[中文](#中文) · [English](#english)

---

<a name="english"></a>
## English

### What this is

**Quant Guru Desk** turns several famous investors' methodologies into a single, summonable AI agent collection. Instead of one repo per person, you install one desk and call whichever guru fits your question. If you don't name one, the desk recommends the best fit.

Each guru is a faithful distillation of a real, public methodology — with their own scoring system, workflow, persona, honest track-record/criticism, and competition output format.

### The roster

| Guru | Style | Best for |
|------|-------|----------|
| **Serenity** (@aleabitoreddit) | Narrative + supply-chain chokepoints | "Who controls the scarce layer?" — AI semis/photonics/CPO, bottleneck hunting |
| **Beth Kindig** (I/O Fund) | Fundamental + forward-revenue modeling | Valuation discipline, forward earnings models, AI compute→memory→power→software leaders |
| **Cathie Wood** (ARK Invest) | Thematic + disruptive innovation | 5-year exponential bets, Wright's Law cost curves, robotics/genomics/blockchain-equity/AI |

*Extensible — add new gurus over time (see below).*

### How to summon

- **By name:** "用 Cathie 分析 $TSLA" · "Serenity 跑一下" · "Kindig 看看 $NVDA" · "木头姐跑一下"
- **By question (auto-recommend):** "这家供应链卡点公司能买吗？" → desk picks Serenity · "NVDA 现在估值贵不贵？" → picks Kindig · "有什么颠覆性的 5 年大机会？" → picks Cathie
- **Panel / 会诊:** "让几位大神会诊一下 $AMD" → multiple gurus debate the same name, with consensus + divergence
- **Competition mode:** "AI投资竞赛" → daily decision in the shared competition format, in the chosen guru's voice

### Structure

```
quant-guru-desk/
├── SKILL.md                    # The desk: roster + router + smart-recommend + panel mode
├── CHANGELOG.md                # Version history
├── CONTRIBUTING.md             # How to contribute / add new gurus
├── dashboard/
│   └── index.html              # Competition visualization dashboard (Chart.js)
├── evals/
│   └── test-cases.md           # 10 behavioral test cases (release gate)
├── examples/
│   ├── daily-run-serenity.md   # Serenity daily-run output demo
│   ├── panel-mode-amd.md       # Three-guru panel debate demo
│   └── competition-day5.md     # Competition Day 5 output demo
├── scripts/
│   ├── scorecard.py            # Local scoring tool (Python 3.9+, zero deps)
│   └── gf_dma.py              # GF-DMA health index calculator (Python 3.9+, zero deps)
├── shared/
│   ├── bayesian-valuation.md   # Bayesian intrinsic growth valuation tool
│   ├── competition-rules.md    # Competition rules + exact output format
│   ├── dialogue-protocol.md    # 5-level teaching ladder for Learn mode
│   ├── evidence-standards.md   # Three-tier evidence ladder + citation rules + red flags
│   ├── market-sources.md       # Cross-market information source playbook (7 markets)
│   └── price-fetching.md       # Price fallback chain + conflict/split checks
└── gurus/
    ├── serenity/      (SKILL.md + references/)   # supply-chain chokepoints
    ├── beth-kindig/   (SKILL.md + references/)   # forward-revenue fundamentals
    └── cathie-wood/   (SKILL.md + references/)   # disruptive innovation / Wright's Law
```

### Install

Clone the repository first, then set up for your platform:

```bash
git clone https://github.com/chuehjen/quant-guru-desk.git
```

---

#### QoderWork

```bash
git clone https://github.com/chuehjen/quant-guru-desk.git ~/.qoderwork/skills/quant-guru-desk
```

Or copy the folder into `~/.qoderwork/skills/`, or drag the `.skill` package into QoderWork. The skill is immediately available via `/quant-guru-desk` or by mentioning any guru name.

---

#### Claude Code

```bash
cp -R quant-guru-desk ~/.claude/skills/quant-guru-desk
```

Claude Code reads `SKILL.md` from `~/.claude/skills/<name>/` automatically. Use slash commands or mention a guru name to activate.

---

#### OpenAI Codex CLI

Codex discovers instructions via `AGENTS.md` files. Two approaches:

**Option A — Symlink as a skill folder (recommended):**
```bash
ln -s $(pwd)/quant-guru-desk ~/.codex/skills/quant-guru-desk
```

**Option B — Reference in your global AGENTS.md:**
```bash
# In ~/.codex/AGENTS.md, add:
echo '## Skills
Read ~/.codex/skills/quant-guru-desk/SKILL.md for the quant-guru-desk investment agent collection.' >> ~/.codex/AGENTS.md
```

Codex will follow the reference chain from SKILL.md → guru sub-files → shared resources.

---

#### Cursor IDE

Cursor uses `.cursor/rules/` for project-level rules (`.mdc` format with YAML frontmatter).

**Option A — Global rule (available in all projects):**

Create `~/.cursor/rules/quant-guru-desk.mdc`:
```markdown
---
description: "Quant Guru Desk — summon investing-guru agents for stock analysis"
globs: "*"
alwaysApply: false
---

When the user asks for stock analysis, guru analysis, or mentions Serenity/Kindig/Cathie/会诊/投资竞赛, read and follow the instructions in:
~/.cursor/skills/quant-guru-desk/SKILL.md
```

Then clone the skill:
```bash
git clone https://github.com/chuehjen/quant-guru-desk.git ~/.cursor/skills/quant-guru-desk
```

**Option B — Project-level (include in a repo):**
```bash
cp -R quant-guru-desk .cursor/skills/quant-guru-desk
```
Add a rule file at `.cursor/rules/quant-guru-desk.mdc` referencing `.cursor/skills/quant-guru-desk/SKILL.md`.

---

#### Windsurf (Codeium)

Windsurf uses `.windsurf/rules/` (modern format) or global rules via Settings.

**Option A — Global rule (recommended):**

1. Open Windsurf → Settings → Cascade → Global Rules
2. Add:
```
When the user asks for stock analysis or mentions Serenity/Kindig/Cathie/会诊/投资竞赛, read and follow: ~/.windsurf/skills/quant-guru-desk/SKILL.md
```
3. Clone the skill:
```bash
git clone https://github.com/chuehjen/quant-guru-desk.git ~/.windsurf/skills/quant-guru-desk
```

**Option B — Project-level:**

Create `.windsurf/rules/quant-guru-desk.md`:
```markdown
---
trigger: glob
globs: ["*"]
---

For investment analysis tasks, read .windsurf/skills/quant-guru-desk/SKILL.md and follow the guru methodology.
```

---

#### Cline / Roo Code (VS Code)

Cline uses `~/Documents/Cline/Rules/` for global rules and `.clinerules/` for project-level.

**Global setup:**
```bash
# 1. Clone the skill
git clone https://github.com/chuehjen/quant-guru-desk.git ~/Documents/Cline/Skills/quant-guru-desk

# 2. Create a global rule file
cat > ~/Documents/Cline/Rules/quant-guru-desk.md << 'EOF'
# Quant Guru Desk

When the user asks for stock analysis, guru analysis, or mentions
Serenity / Kindig / Cathie / 会诊 / 投资竞赛 / 大神事务所:

Read and follow ~/Documents/Cline/Skills/quant-guru-desk/SKILL.md
EOF
```

**Project-level:**
```bash
cp -R quant-guru-desk .clinerules/quant-guru-desk
```

---

#### GitHub Copilot

Copilot reads `.github/copilot-instructions.md` for repository-wide context.

```bash
# In your project's .github/copilot-instructions.md, add:
cat >> .github/copilot-instructions.md << 'EOF'

## Investment Analysis (Quant Guru Desk)

For stock analysis and investment research tasks, reference the quant-guru-desk
skill at: ~/.github/skills/quant-guru-desk/SKILL.md

Follow the guru routing logic: Serenity for supply-chain bottlenecks,
Beth Kindig for forward-revenue modeling, Cathie Wood for disruptive innovation.
Panel mode for multi-guru debate.
EOF
```

Clone globally:
```bash
git clone https://github.com/chuehjen/quant-guru-desk.git ~/.github/skills/quant-guru-desk
```

> **Note:** Copilot cannot directly read external files at runtime. The instructions above serve as context hints — for full functionality, paste key sections of SKILL.md into `copilot-instructions.md` or use Copilot Chat's `@workspace` with the skill folder in your project.

---

#### Universal install (any agent that reads markdown)

For any AI agent that supports custom instruction files:

```bash
git clone https://github.com/chuehjen/quant-guru-desk.git <agent-skills-path>/quant-guru-desk
```

Point your agent's system prompt or instruction file to `SKILL.md` in the cloned directory. The skill is self-contained — SKILL.md references `gurus/*/SKILL.md` and `shared/*.md` via relative paths.

### Adding a new guru

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide. In short:

1. Create `gurus/<new-guru>/SKILL.md` (frontmatter + router + methodology + scoring + persona + hard rules + references table).
2. Add `gurus/<new-guru>/references/` (framework, scoring-system, holdings, track-record, glossary, competition-format).
3. Add the guru to the roster table and smart-recommendation mapping in the root `SKILL.md`, and to this README.
4. Distill the *real* methodology, cite sources, and include an honest track-record/criticism section.
5. Verify all `evals/test-cases.md` still pass.

### Quality guarantees (v1.1+)

- **Evidence grading** — Every data point is labeled Strong/Medium/Weak with source attribution. No more hallucinated numbers.
- **Arithmetic identity** — Every competition output passes `Σ市值 + 现金 = 总资产`. Catches the #1 LLM math error.
- **Behavioral tests** — 10 test cases gate every release. The skill cannot ship if it hallucinates, gives buy/sell instructions, or blends guru voices.
- **Red-flag disclosure** — Mandatory risk callouts when evidence is weak, accounting is suspicious, or a short report exists.

### Tools & enhancements (v2.0+)

- **Cross-market sources** — 7-market playbook (US/A-shares/HK/Taiwan/Japan/Korea/Europe) for tracing non-US supply chain evidence.
- **Bayesian valuation** — Shared tool to separate intrinsic growth from FOMO/narrative. Any guru can invoke it for "is the growth priced in?" questions.
- **GF-DMA health index** — Python CLI to score whether a stock's price trend is supported by fundamental growth (0-100, 6 states).
- **Competition dashboard** — Drop-in HTML file to visualize guru portfolio performance over time (Chart.js).

### Acknowledgments

Each guru's methodology is distilled from public sources and credited inside its own folder. Not affiliated with any of the investors named.

### Disclaimer

For information tracking and research only. **Not investment advice.** Do your own due diligence.

### License

[MIT](LICENSE)

---

<a name="中文"></a>
## 中文

### 这是什么

**Quant Guru Desk（量化大神事务所）** 把多位知名投资人的方法论收进同一个可召唤的 AI agent 集合。不再是"一人一个仓库"——你只装一个事务所，需要谁就召唤谁。不点名时，事务所会根据你的问题智能推荐最合适的大神。

每位大神都是对真实公开方法论的忠实蒸馏，各自带有评分体系、工作流、人格、诚实的业绩/争议说明，以及统一的竞赛输出格式。

### 大神花名册

| 大神 | 风格 | 擅长 |
|------|------|------|
| **Serenity**（@aleabitoreddit） | 叙事 + 供应链卡点 | "谁掌控稀缺环节"——AI 半导体/光子/CPO、瓶颈狩猎 |
| **Beth Kindig**（I/O Fund） | 基本面 + 前瞻营收建模 | 估值纪律、前瞻盈利模型、算力→存储→电力→软件龙头 |
| **Cathie Wood**（ARK Invest） | 主题 + 颠覆式创新 | 5 年指数级机会、Wright's Law 成本曲线、机器人/基因/区块链股权/AI |

*可扩展——后续可持续加入新大神。*

### 怎么召唤

- **点名：** "用 Cathie 分析 $TSLA" · "Serenity 跑一下" · "Kindig 看看 $NVDA" · "木头姐跑一下"
- **按问题（自动推荐）：** 问供应链卡点→Serenity；问估值贵不贵→Kindig；问颠覆性 5 年机会→Cathie
- **会诊：** "让几位大神会诊一下 $AMD" → 多位同题 PK，给共识与分歧
- **竞赛模式：** "AI投资竞赛" → 按统一竞赛格式、以所选大神的口吻出每日决策

### 安装

```bash
git clone https://github.com/chuehjen/quant-guru-desk.git
```

| 平台 | 安装路径 | 备注 |
|------|---------|------|
| **QoderWork** | `~/.qoderwork/skills/quant-guru-desk` | 即装即用，支持 `/quant-guru-desk` 调用 |
| **Claude Code** | `~/.claude/skills/quant-guru-desk` | 自动识别 SKILL.md |
| **OpenAI Codex** | `~/.codex/skills/quant-guru-desk` | 或在 `~/.codex/AGENTS.md` 中引用 |
| **Cursor** | `~/.cursor/skills/quant-guru-desk` | 需配合 `.cursor/rules/*.mdc` 规则文件 |
| **Windsurf** | `~/.windsurf/skills/quant-guru-desk` | 通过 Global Rules 或 `.windsurf/rules/` 引用 |
| **Cline / Roo** | `~/Documents/Cline/Skills/quant-guru-desk` | 配合 `~/Documents/Cline/Rules/*.md` |
| **GitHub Copilot** | `~/.github/skills/quant-guru-desk` | 在 `.github/copilot-instructions.md` 中引用 |

详细的逐平台安装说明见英文 [Install](#install) 部分。

### 质量保证（v1.1+）

- **证据分级** — 每个数据点标注 Strong/Medium/Weak + 来源。杜绝 AI 编造数据。
- **算术恒等校验** — 每次竞赛输出强制通过 `Σ市值 + 现金 = 总资产`。
- **行为测试** — 10 个测试用例把关每次发布，不通过不上线。
- **红旗披露** — 证据薄弱、会计可疑、做空报告存在时强制风险提示。

### 工具增强（v2.0+）

- **跨市场信息源** — 7 市场手册（美/A股/港/台/日/韩/欧），追溯非美供应链证据。
- **贝叶斯估值** — 共享工具，分离内在增长与 FOMO/叙事溢价。任意大神可调用。
- **GF-DMA 健康指数** — Python CLI 评估股价走势是否有基本面支撑（0-100 分，6 种状态）。
- **竞赛看板** — 一个 HTML 文件，粘贴 JSON 即可可视化各大神组合历史表现。

### 免责声明

仅作信息跟踪与研究用途，**不构成投资建议**。请以自己的尽调为准。

### 许可

[MIT](LICENSE)
