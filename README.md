# Quant Guru Desk 🏛️

> A desk of distilled investing-guru AI agents. Summon any famous investor to analyze a stock, build a portfolio, or run a daily competition decision — in their authentic style. One project, many gurus.

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
├── shared/
│   ├── competition-rules.md    # Competition rules + exact output format (single source of truth)
│   └── price-fetching.md       # Price fallback chain + conflict/split checks
└── gurus/
    ├── serenity/      (SKILL.md + references/)   # supply-chain chokepoints
    ├── beth-kindig/   (SKILL.md + references/)   # forward-revenue fundamentals
    └── cathie-wood/   (SKILL.md + references/)   # disruptive innovation / Wright's Law
```

### Install

**QoderWork:**
```bash
git clone <repo-url> ~/.qoderwork/skills/quant-guru-desk
```
Or copy the folder into `~/.qoderwork/skills/`, or drag the `.skill` package into QoderWork.

**Claude Code / Codex:**
```bash
cp -R quant-guru-desk ~/.claude/skills/      # Claude Code
cp -R quant-guru-desk ~/.codex/skills/       # Codex
```

### Adding a new guru

1. Create `gurus/<new-guru>/SKILL.md` (frontmatter + router + methodology + scoring + persona + hard rules + references table).
2. Add `gurus/<new-guru>/references/` (framework, scoring-system, holdings, track-record, glossary, competition-format).
3. Add the guru to the roster table and smart-recommendation mapping in the root `SKILL.md`, and to this README.
4. Distill the *real* methodology, cite sources, and include an honest track-record/criticism section.

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
git clone <repo-url> ~/.qoderwork/skills/quant-guru-desk    # QoderWork
cp -R quant-guru-desk ~/.claude/skills/                     # Claude Code
```

### 免责声明

仅作信息跟踪与研究用途，**不构成投资建议**。请以自己的尽调为准。

### 许可

[MIT](LICENSE)
