# AI Supply Chain Map

A 10-layer map of the AI hardware supply chain with concentration data and key tickers. Use this to walk the value chain and identify bottleneck layers.

Data sources: [Epoch AI Chip Components Explorer](https://epoch.ai/data/ai-chip-components), [OECD Semiconductor Value Chain](https://www.oecd.org/en/publications/mapping-the-semiconductor-value-chain_4154cdbf-en.html), [semiconstocks.com](https://semiconstocks.com).

---

## Layer 1: Raw Materials & Substrates

| Sub-domain | Key companies | Concentration | Tickers |
|-----------|--------------|--------------|---------|
| Silicon wafers | Shin-Etsu, SUMCO | Top 2 > 60% | — |
| Compound semiconductor substrates | AXT Inc (InP/GaAs), Coherent, Wolfspeed (SiC) | Highly concentrated | **AXTI**, WOLF |
| Specialty gases | Air Liquide, Linde, Air Products | Top 3 > 80% | — |
| Photoresist/chemicals | JSR, Tokyo Ohka Kogyo, Shin-Etsu | Japan-dominated | — |
| Rare earth/critical minerals | China processing >85% | Extreme | MP |
| SOI substrates | Soitec (near-monopoly) | Single dominant supplier | **SOI** |

## Layer 2: EDA Tools & IP Cores

| Sub-domain | Key companies | Concentration | Tickers |
|-----------|--------------|--------------|---------|
| EDA tools | Synopsys, Cadence, Siemens EDA | Top 3 > 90% | SNPS, CDNS |
| IP cores | ARM, Synopsys, Cadence | ARM dominant | ARM |

## Layer 3: Semiconductor Equipment

| Sub-domain | Key companies | Concentration | Tickers |
|-----------|--------------|--------------|---------|
| EUV lithography | ASML | **100% monopoly** | ASML |
| DUV lithography | ASML, Canon, Nikon | ASML > 80% | — |
| Etch | Lam Research, Tokyo Electron, Applied Materials | Top 3 > 90% | LRCX |
| Deposition (CVD/PVD) | Applied Materials, Lam Research, Tokyo Electron | Top 3 > 85% | AMAT |
| Inspection/metrology | KLA, Applied Materials, Hitachi | KLA leading | KLAC |
| Ion implant | Applied Materials | Dominant | AMAT |
| SiC testing | Aehr Test Systems | Niche leader | **AEHR** |

## Layer 4: Chip Design

| Sub-domain | Key companies | Notes | Tickers |
|-----------|--------------|-------|---------|
| GPU | NVIDIA (~75-86% AI GPU share) | Absolute dominant | NVDA |
| AI ASIC | Broadcom, Marvell | Custom chip co-design | AVGO, **MRVL** |
| Custom AI chips | Google (TPU), AWS (Trainium) | Internal use | — |
| Network chips | Broadcom (Tomahawk), Marvell | AI cluster interconnect | AVGO, **MRVL** |
| FPGA | AMD (Xilinx), Intel (Altera) | — | AMD |
| Edge/AI SoC | Raspberry Pi, Navitas (GaN) | Edge computing | **RPI**, **NVTS** |

## Layer 5: Wafer Foundry

| Company | Advanced node share | Notes | Tickers |
|---------|-------------------|-------|---------|
| TSMC | **~70%** global, **92%** < 10nm | Core bottleneck | TSM |
| Samsung | ~7% advanced | — | — |
| Tower Semiconductor | Niche photonics foundry | "TSM of photonics" | **TSEM** |
| X-FAB | Only high-volume SiC foundry in US | Government-stamped criticality | **XFAB** |
| GlobalFoundries | Mature nodes, acquired AdvanTech for SiPh | — | GFS |

## Layer 6: Advanced Packaging — CURRENT BIGGEST BOTTLENECK

CoWoS 2026 capacity allocation (~1M wafers):
- NVIDIA: 60% (~595K)
- Broadcom: 15% (~150K)
- AMD: 11% (~105K)
- Others: 14% (~140K)

| Role | Companies | Notes |
|------|-----------|-------|
| CoWoS processing | TSMC (internal), ASE, Amkor | TSMC outsources to ASE/Amkor |
| ABF substrates | Unimicron, Ibiden, Shinko Electric, AT&S | Critical material for advanced packaging |
| Optical packaging/test | Shunsin (6451, Foxconn subsidiary) | "Follow who does the work" |

## Layer 7: HBM Memory — SECOND BIGGEST BOTTLENECK

| Company | HBM share (2025 H2) | Notes | Tickers |
|---------|-------------------|-------|---------|
| SK Hynix | ~50-70% | Absolute leader | — |
| Samsung | Target >30% (2026) | Catching up | — |
| Micron | ~10-15% | Only US HBM supplier | **MU** |

Key stat: The 4 major AI chip designers consume ~90% of global CoWoS and HBM supply (Epoch AI).

## Layer 8: Optical Interconnect / CPO — EMERGING BOTTLENECK (Serenity's current focus)

| Sub-domain | Companies | Role | Tickers |
|-----------|-----------|------|---------|
| Laser/light source | **Sivers Semiconductor** | CPO laser, sole/primary source | **SIVE** |
| Lasers | Lumentum, Coherent | Light sources | **LITE**, **COHR** |
| Transceivers/modules | AAOI, Coherent, Innolight | Optical transceivers | **AAOI**, **COHR** |
| Silicon photonics foundry | TSMC (COUPE), Tower Semi, GlobalFoundries | Photonics chip fab | **TSEM**, GFS |
| FAU/connectors | Multiple specialty suppliers | Fiber array units | — |
| Fiber/cable | Corning, Prysmian, Furukawa | Physical fiber | **GLW** |
| CPO platform chips | Broadcom, NVIDIA, Marvell | Switch + CPO integration | AVGO, **MRVL** |

Key stat: Meta research shows CPO can achieve 65% power savings vs pluggable optics.

## Layer 9: Data Center Infrastructure

| Sub-domain | Companies | Tickers |
|-----------|-----------|---------|
| Liquid cooling CDU | Vertiv, Modine, Schneider | **VRT**, **MOD** |
| Power equipment | Eaton | **ETN** |
| Transmission construction | Quanta Services | **PWR** |
| Nuclear power | Constellation Energy, GE Vernova, Cameco | **CEG**, **GEV**, **CCJ** |
| LNG/energy | Cheniere Energy, Chevron | **LNG**, **CVX** |

## Layer 10: Hyperscale Cloud / End Users

AWS, Google Cloud, Microsoft Azure, Meta, Apple — the demand drivers. Not typically investable through this methodology (too large, too diluted).

---

## Serenity's Ticker Universe (38 names)

### Core photonics/optical (Phase 2-3 active)
AXTI, SIVE, AAOI, LITE, COHR, MRVL, TSEM, SOI, AEHR, GLW, XFAB

### Memory (Phase 1, mostly done)
MU, SNDK

### AI compute/chips
ARM, NVTS, WOLF, RPI, NBIS, CRWV

### Energy (data center power thesis)
LNG, CVX, CEG, NEXT

### Crypto/Web3 (adjacent infrastructure)
ETH, COIN (Coinbase), IREN, RDDT

### Tactical/hedging
SQQQ (3x short QQQ), UVIX (2x VIX), FAZ (3x short financials), GUSH (2x oil/gas)

### Materials
MP (rare earth)

### Other
AIRO, BOT, VLN

---

## Supply chain concentration risk (key stats)

| Bottleneck | Concentration | Data |
|-----------|--------------|------|
| EUV lithography | ASML **100%** | Only supplier globally, 30-year ecosystem |
| Advanced foundry (<10nm) | TSMC **92%** | 100% in Taiwan + Korea |
| CoWoS packaging | TSMC dominant | 4 designers consume 90% of capacity |
| EDA tools | Top 3 **>90%** | Synopsys + Cadence + Siemens |
| HBM memory | 3 suppliers only | SK Hynix 50-70%, Samsung, Micron |
| Silicon wafers | Top 2 **>60%** | Shin-Etsu + SUMCO |
| East Asia concentration | **75%** of capacity | 100% advanced nodes in TW + KR |
