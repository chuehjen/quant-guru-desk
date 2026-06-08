# Market Sources Playbook (shared)

A cross-market reference for finding evidence when analyzing companies listed outside the US or when US-listed companies have significant non-US operations. The desk's competition universe is NYSE/NASDAQ only, but research often requires non-US sources to understand supply chains.

## United States (Primary market)

| Source type | Where to look | Notes |
|-------------|--------------|-------|
| SEC filings | [EDGAR](https://www.sec.gov/cgi-bin/browse-edgar) | 10-K, 10-Q, 8-K, proxy, S-1. **Gold standard** for US companies |
| Earnings transcripts | Seeking Alpha, The Motley Fool, company IR | Verbatim; search for keywords like "sole source", "capacity", "backlog" |
| Insider transactions | SEC Form 4 via EDGAR | Cluster buys/sells near catalysts |
| Short interest | FINRA, Ortex, S3 Partners | High SI + chokepoint thesis = squeeze potential |
| Patent filings | [USPTO](https://www.uspto.gov/) | Technology validation; search by assignee |
| Industry data | SIA, SEMI, Yole, TrendForce, Epoch AI | Semiconductor-specific market sizing |
| News/media | Bloomberg, Reuters, CNBC, WSJ | Medium-tier evidence; cite with date |
| Government | CHIPS Act awards, DoC, NIST, FCC, EIA | Regulatory filings = Strong evidence |

## A-shares (China mainland)

| Source type | Where to look | Notes |
|-------------|--------------|-------|
| Filings | [CNINFO 巨潮资讯](http://www.cninfo.com.cn) | Annual/quarterly reports, prospectuses |
| Earnings + announcements | CNINFO, 东方财富 (eastmoney.com) | All mandatory disclosures |
| Industry research | 天风/中信/国信 sell-side reports | Tier-1 broker research in Chinese |
| Supply chain tracing | 企查查/天眼查 | Shareholder + customer/supplier relationships |
| Patent | [CNIPA](https://www.cnipa.gov.cn/) | China patent office |
| Government policy | MIIT (工信部), NDRC (发改委), MOST (科技部) | Subsidy/policy signals |
| Consensus estimates | Wind (万得), iFind (同花顺) | Paid terminals; some data on eastmoney free |

**Caution:** A-share filings may have less granularity on segment breakdown. Cross-check customer names via 企查查 supply chain graph.

## Hong Kong

| Source type | Where to look | Notes |
|-------------|--------------|-------|
| Filings | [HKEX SENS](https://www.hkexnews.hk/) | Annual/interim reports, circulars |
| Earnings | HKEX news, company IR | Often bilingual (Chinese + English) |
| Short selling | HKEX daily short selling turnover | Published daily |
| Dual-listed context | Compare HK vs A-share pricing for H/A premium | Arbitrage signals |
| Research | HSBC, CLSA, Jefferies (Asia) | English-language coverage of HK/China tech |

## Taiwan

| Source type | Where to look | Notes |
|-------------|--------------|-------|
| Filings | [MOPS (公開資訊觀測站)](https://mops.twse.com.tw/) | Monthly revenue reports (unique to Taiwan — very timely!) |
| Monthly revenue | MOPS | Published by the 10th of each month; leading indicator |
| Earnings | Company IR, 法說會 transcripts | Often in Mandarin |
| Supply chain | DigiTimes, SEMI Taiwan | AI supply chain intelligence |
| Industry | TSIA (台灣半導體產業協會) | Sector-level data |

**Key advantage:** Taiwan requires monthly revenue disclosure — a uniquely timely signal unavailable in other markets.

## Japan

| Source type | Where to look | Notes |
|-------------|--------------|-------|
| Filings | [EDINET](https://disclosure.edinet-fsa.go.jp/) | Japanese EDGAR equivalent |
| Earnings | Company IR, Nikkei | Often bilingual for major companies |
| Supply chain | Nikkei Asia, semiconstocks.com | Japanese semiconductor equipment + materials |
| Industry | JEITA (電子情報技術産業協会) | Electronics industry data |
| Specialist media | EE Times Japan, Semiconductor Engineering | Technical publications |

**Key companies to track:** Tokyo Electron (TEL), Shin-Etsu, SUMCO, JSR, Renesas, Advantest, Screen Holdings.

## South Korea

| Source type | Where to look | Notes |
|-------------|--------------|-------|
| Filings | [DART (전자공시시스템)](https://dart.fss.or.kr/) | Korean EDGAR equivalent |
| Earnings | Company IR (Samsung, SK Hynix) | Q-by-Q guidance for memory pricing |
| Industry | KSIA (한국반도체산업협회) | Memory/chip production data |
| Memory pricing | DRAMeXchange (TrendForce), iSuppli | HBM/DRAM/NAND contract prices |

**Key focus:** HBM supply (SK Hynix dominance), DRAM/NAND pricing cycles, Samsung foundry competitiveness.

## Europe

| Source type | Where to look | Notes |
|-------------|--------------|-------|
| Filings | National regulators (AMF France, BaFin Germany, FCA UK) | Fragmented across countries |
| Stockholm (SIVE) | [Finansinspektionen](https://fi.se/), Nasdaq Nordic | Swedish-listed; filings in Swedish/English |
| Euronext (SOI, STM) | Euronext.com, AMF (France) | Soitec = French filing + English IR |
| ASML | [AFM Netherlands](https://www.afm.nl/) | Annual report in English; key for EUV equipment data |
| Industry | SEMI Europe, imec | European semiconductor R&D |
| Government | EU Chips Act, European Commission | Subsidy and sovereignty signals |

**Key names for the desk:** ASML (EUV monopoly), Soitec/SOI (SOI substrates), SIVE (CPO lasers), X-FAB (SiC/photonics foundry), STMicroelectronics.

## Cross-market intelligence tips

1. **Monthly Taiwan revenue** is the single most timely public signal for semiconductor supply chains. When TSEM or ASE reports monthly revenue growth, it confirms orders before quarterly earnings.

2. **Japanese equipment orders** (SEMI Japan billings) lead global semiconductor capex cycles by 3-6 months.

3. **Korean memory pricing** (TrendForce contract prices) is the earliest indicator for MU and memory-adjacent plays.

4. **Chinese supply chain mapping** via 企查查 can reveal undisclosed customer/supplier relationships that filings don't mention until they're material.

5. **European sovereignty signals** (EU Chips Act grants) confirm criticality assessments — if a government calls a company "strategic", that's a Strong evidence data point.

## Evidence grading by market

| Market | Strong sources | Medium sources | Caution |
|--------|---------------|---------------|---------|
| US | SEC EDGAR, earnings transcripts | Bloomberg/Reuters, sell-side | Most transparent |
| Taiwan | MOPS monthly revenue, TWSE filings | DigiTimes | Monthly revenue = uniquely timely |
| Japan | EDINET filings | Nikkei Asia | Language barrier; bilingual for top-10 |
| Korea | DART filings | TrendForce memory data | Samsung segment data can be opaque |
| China | CNINFO filings | Broker research | Less segment detail; related-party risk |
| Europe | National regulators | SEMI Europe | Fragmented across 5+ regulators |
| HK | HKEX filings | CLSA/HSBC research | Dual-listed = check both filings |
