# Reflection Protocol — 反思记忆

让大师具有"活人感"：记住自己说过什么，下次遇到同一只票时自动回溯，评估之前判断的对错，并据此调整当前分析的信心度。

## 核心理念

"一个从不回顾自己判断的分析师，和一个从不复盘的交易员一样不值得信任。"

反思记忆解决的问题：
1. 用户问"上次你怎么说的？结果呢？" → 有据可查
2. 同一只票反复分析时，自动注入历史上下文 → 避免前后矛盾
3. 跟踪命中率 → 诚实面对方法论的强项和盲区
4. 让大师人格有时间线 → "三个月前我因为 XX 推荐了 YY，现在回看..."

## 记忆写入时机

每次产出分析（非 Learn 模式）时，在完成输出后，将本次判断写入 memory：

### 触发条件

| 场景 | 是否写入 |
|------|---------|
| 分析具体 ticker（任何模式） | ✅ 写入 |
| 竞赛日报（含交易动作） | ✅ 写入（每个 BUY/SELL 动作一条） |
| 竞赛日报（纯 HOLD 不动） | ❌ 不写入（减少噪音） |
| 会诊模式 | ✅ 写入共识结论（非每个大师单独写） |
| Learn 模式（纯教学） | ❌ 不写入 |
| 宏观分析（Dalio 象限判断） | ✅ 写入（象限变化是重要事件） |

### 记忆格式

使用 QoderWork memory 工具写入，target = "memory"：

```
[QUANT-GURU] [DATE] [GURU] [TICKER] [ACTION] [CONVICTION]
Entry: $[price] | Stop: $[price] | Target: $[price]
Logic: [一句话核心逻辑]
Context: [当时的关键背景，30字内]
```

**示例：**
```
[QUANT-GURU] 2026-06-09 Minervini NVDA BUY 4
Entry: $205 | Stop: $190 | Target: $250
Logic: VCP 3rd contraction complete, pivot $206 breakout on volume
Context: Market Stage 2, AI capex cycle intact
```

```
[QUANT-GURU] 2026-06-09 Buffett COST HOLD 5
Entry: $780 (existing) | Stop: moat impairment | Target: long-term
Logic: Membership renewal 93%+ = unbreakable moat, owner earnings growing 12%
Context: Consumer resilient, pricing power intact
```

```
[QUANT-GURU] 2026-06-09 Dalio REGIME WATCH 3
Entry: — | Stop: — | Target: —
Logic: Quadrant = Goldilocks but paradigm shift signals rising (2/5 → 3/5)
Context: 10Y yield creeping up, inflation stickier than expected
```

### 宏观记忆（Dalio 专用）

```
[QUANT-GURU] [DATE] Dalio REGIME [QUADRANT] [CONFIDENCE]
Allocation: Equities [X%] / Bonds [X%] / Gold [X%] / Commodities [X%] / Cash [X%]
Logic: [象限判断依据]
Shift risk: [LOW/MEDIUM/HIGH]
```

## 记忆召回时机

### 自动召回（分析前必做）

每次分析一只 ticker 前，用 `memory_search` 查询：

```
query: "QUANT-GURU [TICKER]"
```

如果找到历史记录 → 在分析正文开头插入**回溯块**：

```
### 📝 历史回溯

上次分析: [DATE] by [GURU]
当时判断: [ACTION] @ $[entry], 信心 [X]
当时逻辑: [logic]
实际结果: 当前价 $[current] → [+X% / -X%] from entry
判断评估: ✅ 正确 / ⚠️ 部分正确 / ❌ 错误
经验教训: [一句话]
```

### 判断评估标准

| 结果 | 评估 |
|------|------|
| BUY → 当前 > entry + 10% | ✅ 正确 |
| BUY → 当前在 entry ±10% 内 | ⚠️ 中性（未验证） |
| BUY → 触发止损 或 当前 < entry - 10% | ❌ 错误 |
| SELL → 当前 < sell price | ✅ 正确（卖对了） |
| SELL → 当前 > sell price + 15% | ❌ 错误（卖早了） |
| AVOID → 当前 < 当时价格 | ✅ 正确 |
| AVOID → 当前 > 当时价格 + 20% | ❌ 错误（错过了） |
| WATCH → 后来变成 BUY 且涨了 | ⚠️ 保守但合理 |

### 影响当前分析

历史判断的对错应影响当前分析的信心度：

| 历史情况 | 对当前分析的影响 |
|---------|----------------|
| 同一 ticker 上次判断正确 + 逻辑延续 | 可以提高信心度 +1（论点被验证） |
| 同一 ticker 上次判断错误 + 逻辑未变 | 必须解释"为什么这次不同" / 降低信心度 -1 |
| 同一 ticker 上次判断错误 + 逻辑已变 | 明确说"上次错在 X，这次角度完全不同" |
| 同一大师连续 3 次错误 | 在输出中坦诚："近期命中率偏低，建议缩小仓位或寻求其他大师会诊" |

## 反思摘要（周期性）

当用户问"最近表现怎么样"或"命中率如何"时，用 `memory_search` 拉取所有 `[QUANT-GURU]` 记录，生成摘要：

```
## 📊 反思摘要 — [GURU] — 近 [N] 次判断

| 日期 | Ticker | 动作 | 入场 | 当前 | 收益 | 评估 |
|------|--------|------|------|------|------|------|

命中率: X/N (XX%)
平均收益(正确): +XX%
平均亏损(错误): -XX%
盈亏比: X.X : 1

### 模式识别
- 强项: [什么场景下判断准确率高]
- 弱项: [什么场景下容易犯错]
- 改进: [下次遇到类似情况应该怎么调整]
```

## 记忆管理

### 写入规则
- 每条记忆控制在 3 行内（紧凑）
- 使用 `[QUANT-GURU]` 前缀确保可搜索
- 日期用 ISO 格式 (YYYY-MM-DD)
- 每天每位大师最多写入 5 条（避免 memory 膨胀）

### 清理规则
- 超过 90 天且已评估的记录 → 可归档到 daily memory（非 MEMORY.md）
- 错误判断保留更久（教训比成功更有价值）
- 宏观象限判断永久保留（用于长周期对比）

### 隐私
- 反思记忆属于用户私有
- 会诊模式中不暴露"上次我判断错误"的细节给其他参与者（群聊场景）
- 只在单独分析时完整展示历史回溯
