# Serenity Method — Full Framework (v2)

The detailed rubric behind the methodology. Read this when applying the method to a specific ticker and you need the full analytical structure.

---

## The Nine-Step Research Workflow

This is the expanded workflow for theme scans and deep analysis. The five-step method in SKILL.md is a compressed version.

1. **Set the scope** — Market (US/HK/A/TW/JP/KR/EU), theme (CPO, power semis, robotics, energy), time window (3-12 months for "now")
2. **Translate story into system change** — What technical or economic change is driving demand? Which old design becomes strained? Which physical constraint matters most: power, latency, bandwidth, heat, yield, purity, reliability, cycle time, packaging density, regulation, or grid connection?
3. **Map the value chain** — downstream demand → system integrators → modules/subsystems → chips/devices → process and packaging → equipment and testing → materials and consumables → physical infrastructure. See `supply-chain-map.md` for the 10-layer AI hardware map.
4. **Find the scarce layer** — Look for: low supplier count, long qualification, hard expansion, critical know-how, material purity, specialized equipment, customer certification, long lead times, capacity reservations. Prefer less obvious upstream layers. **Rank the layers before naming companies.**
5. **Build company universe** — At least 20 candidates for broad themes, 5+ for focused themes. Classify each: controls the scarce layer / supplies the scarce layer / benefits from the trend / weak control / mainly has a story.
6. **Gather and grade evidence** — Use the evidence ladder (SKILL.md Step D). Aim for at least 25 sources for deep scans. Primary sources first (filings, transcripts, patents), then media, then social.
7. **Score and rank** — Use the chokepoint scorecard (8+8 factors, see `scoring-system.md`). Keep scarce-layer priority and company priority separate.
8. **Explain what could go wrong** — Cover: substitution, faster competitor expansion, weak demand, dilution, poor margins, governance, geopolitics, customer loss, valuation already pricing in success.
9. **Give the next research move** — Specific checks: filings, metrics, customer cross-checks, capacity evidence, contract evidence, valuation comparison, near-term announcements.

---

## The Three Investment Phases

Serenity divides the AI supply chain into sequential investment phases:

| Phase | Theme | Status | Key Names |
|-------|-------|--------|-----------|
| Phase 1: Memory | HBM, storage | **Done** — most upside captured | MU, SNDK, SK Hynix |
| Phase 2: Optical | Transceivers, lasers, fiber, modules | **Active** — current core | SIVE, AAOI, LITE, COHR, AXTI, GLW |
| Phase 3: Silicon Photonics / CPO | Co-packaged optics, SiPh substrates, foundry | **Emerging** — building positions | SOI, TSEM, MRVL, XFAB, GFS |

**Phase transition signals:** When the current phase names are fully priced (institutional rotation complete, analyst coverage saturated, FUD replaced by consensus), begin moving to the next phase's upstream bottleneck.

---

## 1. Critical-chokepoint discovery (Steps 1-4, expanded)

The edge is **finding the link in a value chain that the market under-prices**.

1. **Pick a durable macro driver.** AI compute growth, 800VDC data-center power, the CPO/photonics "supercycle", supply-chain sovereignty (US/EU vs China).
2. **Walk the value chain to the bottleneck.** Demand flows down until it hits a link where supply is hard to add. E.g. AI compute → data movement → optical interconnect → **laser/light source** becomes the bottleneck.
3. **Identify who is designed-in there.** Certification, "sole source"/"primary source" language, customer reference designs.
4. **Check it's un-priced.** Market cap vs the opportunity. Prefer small/mid caps where the bottleneck role isn't reflected in price.

### OSINT heuristics

- **Government / regulatory filings** — NIST, CHIPS Act 2, Dept. of Commerce. Government language like "only high-volume SiC foundry in America" = criticality stamp.
- **Customer-side moves** — competitor removed from vendor list; transcript phrases: "sole source", "primary source", "design-in", "qualification".
- **Follow who actually does the work** — the headline brand is too diluted. Value sits in the subsidiary or upstream supplier.
- **Corporate-action signals** — M&A hints; board members with M&A/IPO backgrounds; dual-listing / uplisting; capacity-funding raises.
- **Capital-flow catalysts** — MSCI / Nasdaq index inclusion forces passive buying. Real but **non-fundamental**; track separately from quality.
- **Triangulate** — multiple independent signals, not a single headline.

---

## 2. First-principles decomposition (Step 2, expanded)

> Value = future owner cash flows. Always reason from five levers, and **name the strongest and weakest**.

1. **Durability of demand** — structural vs fad. What breaks the demand?
2. **Supply bottleneck** — genuinely scarce? For how long? What ends the scarcity?
3. **Pricing power** — certification, scarcity, switching cost. (60% gross-margin guidance is a signal, not proof.)
4. **Capital intensity** — capex and dilution to grow. Don't judge a foundry on low P/B alone — look at ROIC, utilization, gross margin.
5. **Rule-of-law / geopolitics** — property rights, subsidies, jurisdiction, sovereignty exposure.

A bottleneck asset's value rests on: **customers must have it** + **others can't supply it short-term**. If both hold → pricing power + capacity premium.

---

## 3. Buffett quality gate (Step 3, the exact rubric)

Every field starts at `unverified`. **Escalate only with cited evidence** from financials, transcripts, or filings. A single tweet is never evidence for "strong" or "proven".

- **护城河 (moat)** — `unverified` → `weak/medium/strong` with a one-sentence reason (certification, switching cost, IP, scale, regulatory barrier).
- **赚钱能力 (profitability)** — `unverified` → `improving/proven` only when revenue, gross margin, or cash-flow numbers are cited. Guidance = `improving` at best.
- **客户替换风险** — `unverified` → `low/medium/high` (certification cycle, second-source availability, customer concentration).
- **Buffett 式好公司** — `not yet` by default. `yes` needs moat + profitability + sane capital allocation all above `unverified`.
- **当前结论** — `证据不足` by default. `研究地图` when there's a lead worth tracking. `可投资结论` requires moat + financials + valuation + margin-of-safety.

---

## 4. Narrative-vs-fundamentals hygiene (Step 4, expanded)

- **Doubt ladder** — bears move goalposts, each gets falsified, stock re-rates. Re-rating ≠ proven fundamentals.
- **Media FUD** — "meme/scam/overvalued" is sentiment, not analysis.
- **Capital flows / squeezes** — positioning catalysts, not value. Keep out of moat/profitability fields.
- **Virality / track record** — context, not company quality.

**Rule:** anything here may appear as context, but may **not** lift a Buffett field above `unverified`.

---

## 5. Selection signature (empirical patterns)

Recurring traits of picks that fit the methodology:
- Chokepoint / sole-or-primary source at a real bottleneck
- Small/mid-cap, un-priced vs the opportunity (<$3B)
- Contrarian setup — high short interest and/or active media FUD
- A dated catalyst (~1-4 quarters out)
- First-principles, self-computed case

### Theme-rotation logic

The observed rotation pattern:
1. **UP the supply chain** — end-product → component → material → material's material
2. **EARLIER in the cycle** — front-run unmapped catalysts
3. **SMALLER / less-covered** — the subsidiary, not the headline brand

### Catalyst playbook

- ETF approvals / filings
- Index inclusion → forced passive flows
- Earnings supply-chain read-throughs
- Government / regulatory filings
- M&A / board changes / dual-listing / private placements
- Short-squeeze setups (very high short interest)

### Conviction tells

When graduating a name to a core position:
- Mention-velocity ramp (repeated coverage over days)
- Position-size language ("bought $Xk", "scaling to $Y")
- Repeated defense vs FUD
- Supply-chain cross-linking (ties name into broader chokepoint map)

### Anti-patterns (what to avoid)

- Zero-revenue hype at huge caps
- Heavy serial dilution (ATMs as overhangs)
- Paywalled "gurus" / snake-oil TA
