# Cross-Market Data Sources

Source paths by market for supply-chain OSINT research. Adapted from [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill).

## US Stocks (primary market for this skill)

**Primary sources (Strong evidence):**
- SEC filings: 10-K, 10-Q, 8-K, S-1, S-3, Form 4
- Earnings call transcripts (Seeking Alpha, company IR)
- Investor presentations
- Patent databases (USPTO, Google Patents)

**Key checks:**
- ATM/S-3 → dilution risk
- Form 4 → insider transactions
- 8-K → material events, contracts, board changes
- Customer concentration in 10-K risk factors
- Estimate gaps (few/no analysts covering = information edge)

## A-Shares (China mainland)

**Primary sources:**
- 年报、半年报、季报、临时公告 (annual/semi/quarterly/ad-hoc reports)
- 交易所问询函 (exchange inquiry letters — gold for supply-chain verification)
- 互动易 / 上证e互动 (investor Q&A platforms)
- 招投标 (government procurement bids)
- 环评/能评 (environmental/energy assessments — reveal capacity plans)
- 地方项目备案 (local project filings)
- 海关数据 (customs data — export volumes)

**Key checks:**
- 应收账款/存货增速 vs 收入增速 (receivables/inventory vs revenue growth)
- 关联交易 (related-party transactions)
- 合同负债 (contract liabilities = advance payments = demand signal)
- 现金流 (cash flow quality)

## Hong Kong

**Primary sources:**
- HKEX filings (annual/interim reports, announcements)
- Placings and subscriptions (dilution signals)
- Connected transactions
- Southbound Connect eligibility (passive flow catalyst)

**Key checks:**
- Mainland policy exposure
- Liquidity (many HK small-caps are illiquid)
- Dual-listing / uplisting timeline

## Taiwan

**Primary sources:**
- MOPS (Market Observation Post System) filings
- Monthly revenue data (unique to Taiwan — very timely)
- Company IR materials

**Key checks:**
- Customer concentration (many TW companies depend on 1-2 hyperscalers)
- FX sensitivity (NTD movements)
- Cross-strait geopolitical risk
- "Follow who does the work" — subsidiaries of large TW conglomerates

## Japan

**Primary sources:**
- TDnet (Timely Disclosure network) filings
- Company IR, annual reports
- Trade journals (Nikkan Kogyo, etc.)

**Key checks:**
- Conservative guidance culture (Japanese companies under-promise)
- Cross-shareholding structures
- Low analyst coverage (information edge possible)

## Korea

**Primary sources:**
- DART (Data Analysis, Retrieval and Transfer System) filings
- Export statistics (Korea Customs Service)
- Company IR

**Key checks:**
- Large customer dependency (Samsung/SK ecosystem)
- Memory cycle exposure
- Won FX sensitivity

## Europe

**Primary sources:**
- Local exchange filings (Euronext, LSE, Deutsche Börse)
- EU subsidy / CHIPS Act project filings
- Company IR, annual reports

**Key checks:**
- M&A / option structures (European companies often have complex structures)
- Liquidity (many European small-caps trade thinly)
- Sovereignty policy tailwinds (EU CHIPS Act, IPCEI)

## Universal Sources

**Supply-chain mapping tools:**
- [Epoch AI Chip Components Explorer](https://epoch.ai/data/ai-chip-components) — AI chip capacity tracking
- [semiconstocks.com](https://semiconstocks.com) — Serenity ticker tracker
- [DeepTracker](https://www.deeptracker.ai) — Knowledge graph supply chain risk mapping
- [TechInsights](https://www.techinsights.com) — Semiconductor teardown and compliance
- [OECD Semiconductor Value Chain report](https://www.oecd.org/en/publications/mapping-the-semiconductor-value-chain_4154cdbf-en.html) — Concentration analysis

**Government/policy:**
- NIST CHIPS Act filings and blueprints
- US Department of Commerce export control filings
- EU CHIPS Act / IPCEI project documents
- National security reviews (CFIUS, etc.)
