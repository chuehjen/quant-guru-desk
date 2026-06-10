# Quant Guru Desk 🏛️

> A desk of distilled investing-guru AI agents. Summon any famous investor — get a thesis, a conviction score, a position call, and **a permanent record that gets graded against the market 30/90 days later.**

**v2.1.0** · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [Install for other agents](docs/install.md)

[中文](#中文) · [English](#english)

---

<a name="english"></a>
## English

### What this is

A single skill that summons distilled investing-guru AI agents. Each guru is a faithful distillation of a real, public methodology — with its own scoring system, persona, honest track-record, and competition output format.

What makes this different from "another prompt-pack of personalities":

> Every signal the desk emits is appended to `calls.json` and **graded against actual price 30 / 90 days later**. The skill keeps a public batting average. Anyone can run `scripts/track_calls.py summary` and see whether the gurus are actually right. *(see [Reflection-as-core](#reflection-as-core))*

### The roster

| Guru | Style | Best for |
|------|-------|----------|
| **Warren Buffett** (Berkshire) | Value + moat + owner earnings | "Is this a wonderful business at a fair price?" — moat durability, margin of safety, 10-year hold |
| **Ray Dalio** (Bridgewater) | Macro-systematic + risk parity | "Where are we in the cycle?" — debt cycle, regime quadrant, All-Weather allocation |
| **Beth Kindig** (I/O Fund) | Fundamental + forward-revenue modeling | Valuation discipline, forward earnings models, AI compute→memory→power→software leaders |
| **Cathie Wood** (ARK Invest) | Thematic + disruptive innovation | 5-year exponential bets, Wright's Law cost curves, robotics/genomics/AI |
| **Serenity** (@aleabitoreddit) | Narrative + supply-chain chokepoints | "Who controls the scarce layer?" — AI semis/photonics/CPO bottleneck hunting |
| **Mark Minervini** (SEPA) | Momentum + technical timing | "WHEN to buy?" — Stage 2 uptrends, VCP entries, strict stop-losses |

The roster is intentionally frozen at 6 — four orthogonal lenses (value / macro / growth / timing) plus two specialist growth angles (chokepoint / disruption). **Adding more gurus is the lowest-value, easiest-to-fork direction; we are not doing it.**

### How to summon

- **By name** — "用 Cathie 分析 $TSLA" · "Serenity 跑一下" · "Kindig 看看 $NVDA" · "Buffett 看 KO" · "Dalio 现在什么象限" · "Minervini 看 NVDA 时机"
- **By question (auto-recommend)** — supply-chain question → Serenity · valuation question → Kindig · 5-year disruption question → Cathie · "is it cheap" → Buffett · macro/regime → Dalio · entry timing → Minervini
- **Panel / 会诊** — "让几位大神会诊一下 $AMD" → multiple gurus debate the same name, output consensus + divergence
- **Combo / 组合** — 🧪 deprecated until Panel proves out a >55% hit rate. See [calls.json](#reflection-as-core).
- **Competition mode** — "AI 投资竞赛" → daily decision in shared format, in the chosen guru's voice

### <a name="reflection-as-core"></a>Reflection-as-core

This is the heart of the project. Without it the desk is just role-play.

```
You analyze NVDA today                    →   appended to calls.json
30 days later                             →   scripts/track_calls.py score
                                              fetches Twelve Data, grades the call
90 days later                             →   second grade, more weight
Anytime                                   →   scripts/track_calls.py summary
                                              prints per-guru hit rate, average win/loss
```

**A call is "correct" if the move agrees with the action by ≥10% within the horizon.** Stop-outs and missed targets are graded honestly, not retroactively explained away. The grader is deterministic — the LLM does not get to grade itself.

```bash
export TWELVEDATA_API_KEY=your_key_here   # free tier works
scripts/track_calls.py summary            # see the desk's batting average
scripts/track_calls.py score              # grade calls that aged past 30/90 days
```

The schema is documented in [`shared/calls-schema.md`](shared/calls-schema.md). The first signal card the desk emits in any conversation also writes a row.

### Install (Quick start)

The skill is platform-agnostic markdown. Two ways to install:

**QoderWork (recommended):**
```bash
git clone https://github.com/chuehjen/quant-guru-desk.git ~/.qoderwork/skills/quant-guru-desk
```
Available immediately via `/quant-guru-desk` or by mentioning any guru name.

**Claude Code:**
```bash
git clone https://github.com/chuehjen/quant-guru-desk.git ~/.claude/skills/quant-guru-desk
```
Slash commands or guru names activate it.

**Anything else (universal):**
```bash
git clone https://github.com/chuehjen/quant-guru-desk.git <agent-skills-path>/quant-guru-desk
```
Point your agent's instruction file at `SKILL.md`. The skill is self-contained — relative paths only.

> Codex / Cursor / Windsurf / Cline / Copilot recipes: see [docs/install.md](docs/install.md).

### Default output is short

Every analysis ends with a 4-line conclusion (one-sentence view, conviction, suggested position, biggest risk). The full evidence-graded signal card is collapsed by default — expand only when you want to dig in. *(See [`shared/signal-card.md`](shared/signal-card.md) for the format.)*

### Quality guarantees

- **Reflection-as-core** — every call lands in `calls.json` and gets graded by price action 30/90 days out. The grader does not negotiate.
- **Evidence grading** — every data point is labeled Strong / Medium / Weak with a source. No hallucinated numbers.
- **Arithmetic identity** — every competition output passes `Σ market value + cash = total assets`. Catches the #1 LLM math error.
- **Behavioral tests** — 10 release-gating test cases. The skill cannot ship if it hallucinates, gives buy/sell instructions, or blends guru voices.
- **Red-flag disclosure** — mandatory risk callouts when evidence is weak, accounting is suspicious, or a short report exists.

### Tools

- **`scripts/track_calls.py`** — append calls, grade calls, print summary. Zero deps beyond Python 3.9 + `urllib`.
- **`scripts/scorecard.py`** — Serenity-style chokepoint scoring CLI.
- **`scripts/gf_dma.py`** — GF-DMA health index (price vs fundamental support, 0–100).
- **`shared/bayesian-valuation.md`** — separate intrinsic growth from FOMO/narrative premium.
- **`dashboard/index.html`** — drop-in HTML to visualize competition portfolio performance (Chart.js).

### Disclaimer

For information tracking and research only. **Not investment advice.** Do your own due diligence.

### License

[MIT](LICENSE)

---

<a name="中文"></a>
## 中文

### 这是什么

把多位知名投资人的方法论收进同一个可召唤的 AI agent 集合。每位大师都是对真实公开方法论的忠实蒸馏——带有评分体系、人格、诚实的业绩说明，以及统一的竞赛输出格式。

**和市面上的"提示词大师包"最大的区别：**

> 每条信号都会被追加到 `calls.json`，并在 **30 / 90 天后用真实股价打分**。事务所有一份公开的命中率账本。任何人都可以跑 `scripts/track_calls.py summary` 看大师们是不是真的判断准确。*（详见 [反思即核心](#反思即核心)）*

### 大神花名册

| 大神 | 风格 | 擅长 |
|------|------|------|
| **Warren Buffett**（伯克希尔） | 价值 + 护城河 + 所有者收益 | "这是不是一家好生意 × 合理价格？" 护城河耐久度、安全边际 30%+、10 年视角 |
| **Ray Dalio**（桥水） | 宏观系统 + 风险平价 | "我们处在周期哪个位置？" 债务周期、象限、All-Weather 配置 |
| **Beth Kindig**（I/O Fund） | 基本面 + 前瞻营收建模 | 估值纪律、前瞻盈利模型、算力→存储→电力→软件龙头 |
| **Cathie Wood**（ARK Invest） | 主题 + 颠覆式创新 | 5 年指数级机会、Wright's Law 成本曲线、机器人/基因/AI |
| **Serenity**（@aleabitoreddit） | 叙事 + 供应链卡点 | "谁掌控稀缺环节"——AI 半导体/光子/CPO、瓶颈狩猎 |
| **Mark Minervini**（SEPA） | 动量 + 技术时机 | "什么时候买？" Stage 2 上升期、VCP 形态、严格止损 |

花名册有意冻结在 6 位——四个正交视角（价值/宏观/成长/时机）+ 两个细分成长角度（卡点/颠覆）。**继续加大师是边际效用最低、最容易被 fork 的方向，所以不做。**

### 怎么召唤

- **点名：** "用 Cathie 分析 $TSLA" · "Serenity 跑一下" · "Kindig 看看 $NVDA" · "Buffett 看 KO" · "Dalio 现在什么象限" · "Minervini 看 NVDA 时机"
- **按问题（自动推荐）：** 供应链卡点→Serenity · 估值贵不贵→Kindig · 颠覆性 5 年机会→Cathie · 够不够便宜→Buffett · 宏观/象限→Dalio · 入场时机→Minervini
- **会诊：** "让几位大神会诊一下 $AMD" → 多人同题 PK，给共识与分歧
- **Combo（组合流程）：** 🧪 已冻结。在 Panel 模式跑出 >55% 命中率之前不投精力。
- **竞赛模式：** "AI 投资竞赛" → 按统一竞赛格式、以所选大神的口吻出每日决策

### <a name="反思即核心"></a>反思即核心

这是项目唯一不能被 fork 的部分。没有它，事务所只是角色扮演。

```
今天分析 NVDA           →   追加一条记录进 calls.json
30 天后                 →   scripts/track_calls.py score
                            自动拉 Twelve Data 历史价 → 打分
90 天后                 →   再打一次分（权重更大）
任何时候                →   scripts/track_calls.py summary
                            按大师列出命中率、平均盈/亏
```

**判定规则：动作在时间窗内得到 ≥10% 验证 = "正确"**。止损出局/错失目标如实记账，不事后找理由。打分是确定性脚本，LLM 没有自己给自己打分的机会。

```bash
export TWELVEDATA_API_KEY=你的_key   # 免费 tier 也能用
scripts/track_calls.py summary       # 看事务所的命中率账本
scripts/track_calls.py score         # 给到期的 call 打分
```

Schema 在 [`shared/calls-schema.md`](shared/calls-schema.md)。事务所每发出一张 signal card 都会写入一行。

### 安装

```bash
# QoderWork（推荐）
git clone https://github.com/chuehjen/quant-guru-desk.git ~/.qoderwork/skills/quant-guru-desk

# Claude Code
git clone https://github.com/chuehjen/quant-guru-desk.git ~/.claude/skills/quant-guru-desk

# 其他读 markdown 的 agent（通用方式）
git clone https://github.com/chuehjen/quant-guru-desk.git <skills-path>/quant-guru-desk
```
让 agent 把 `SKILL.md` 加入指令文件。技能内部全部用相对路径，自包含。

> Codex / Cursor / Windsurf / Cline / Copilot 详细配方见 [docs/install.md](docs/install.md)。

### 默认输出是短的

每次分析以四行短结论收尾（一句话观点 / 信心度 / 建议仓位 / 最大风险）。完整的证据分级 signal card 默认折叠，需要再展开。*格式见 [`shared/signal-card.md`](shared/signal-card.md)*。

### 质量保证

- **反思即核心** — 每条信号都进 `calls.json`，30/90 天后由价格打分。打分脚本不和 LLM 商量。
- **证据分级** — 每个数据点标注 Strong/Medium/Weak + 来源。杜绝编造。
- **算术恒等校验** — 每次竞赛输出强制通过 `Σ市值 + 现金 = 总资产`。
- **行为测试** — 10 个用例把关每次发布，不通过不上线。
- **红旗披露** — 证据薄弱、会计可疑、做空报告存在时强制风险提示。

### 工具

- **`scripts/track_calls.py`** — 追加、打分、汇总。Python 3.9+ 零依赖。
- **`scripts/scorecard.py`** — Serenity 风格卡点评分 CLI。
- **`scripts/gf_dma.py`** — GF-DMA 健康指数（价格走势 vs 基本面支撑，0-100）。
- **`shared/bayesian-valuation.md`** — 分离内在增长与 FOMO/叙事溢价。
- **`dashboard/index.html`** — 一个 HTML，粘贴 JSON 即可可视化竞赛组合表现。

### 免责声明

仅作信息跟踪与研究用途，**不构成投资建议**。请以自己的尽调为准。

### 许可

[MIT](LICENSE)
