# Research Ideation

> An AI agent skill (OpenCode / WorkBuddy) that turns your literature library into a systematic idea engine.
>
> **Stop waiting for inspiration. Start generating ideas systematically.**

[English](#english) · [中文](#中文)

---

## English

### The Problem

| How most researchers do it | What goes wrong |
|---------------------------|-----------------|
| Random inspiration, hallway chats, advisor says "try this" | **Duplication** — spend weeks, find out it's already published |
| Jump on the first "interesting" idea | **Selection bias** — no objective comparison |
| No systematic exploration method | **Blind spots** — miss entire research directions |

### What This Changes

| Before | After |
|--------|-------|
| "I wonder if this is novel...?" | Literature baseline maps what exists → gaps are your targets |
| "I only have 1-2 ideas" | 6 systematic methods → cover the full possibility space |
| "Is this idea any good?" | 30-point scoring across 6 dimensions → objective comparison |
| "Which idea should I work on?" | Lifecycle tracking (待评估→评估中→进行中→已归档) |

### How It Works

```
1️⃣  You collect papers → put them in 📚 05-文献库/ (one .md per paper)

2️⃣  AI initializes → reads every paper, extracts research directions
    ↓
    📋 索引.md gets populated with: existing directions + gaps (your targets)

3️⃣  Generate ideas (two paths):
    ┌─────────────────────────────────────────────┐
    │  A) Ask AI: "Think of new ideas"            │
    │     → AI uses 想点子指南.md (6 methods)      │
    │     → writes to 待评估点子.md                │
    │     → registers in 索引.md (status: 待评估)   │
    ├─────────────────────────────────────────────┤
    │  B) Write your own idea directly             │
    │     → add to 待评估点子.md                   │
    │     → AI automatically syncs to 索引.md      │
    └─────────────────────────────────────────────┘

4️⃣  Evaluate: "Evaluate: [idea name]"
    → AI researches + uses evaluation template
    → writes white paper in 02-评估中/
    → updates 索引.md with score (status: 评估中)
```

**Key insight**: You can't know what's new until you know what exists. The literature library is your novelty baseline — ideas target gaps, not crowded territory.

### 6 Brainstorming Methods

| # | Method | Core question |
|---|--------|---------------|
| 1 | **Combination Innovation** | Your method + new tech × new domain? |
| 2 | **Fix Weaknesses** | What limitations do survey papers repeat? |
| 3 | **Transplant Methods** | What mature theory from another field fits? |
| 4 | **Theory Deep Dive** | What mathematical properties remain unproven? |
| 5 | **Boundary Limits** | What if your field's default assumptions are wrong? |
| 6 | **Literature Deconstruction** | What "Future Work" gaps did top papers leave? |

### Scoring (30 pts)

| Dimension | Question | Score |
|-----------|----------|:-----:|
| Novelty | Has this been done? | 1-5 |
| Feasibility | Can it be built? | 1-5 |
| Verifiability | Can results be shown? | 1-5 |
| Publishability | Will reviewers buy it? | 1-5 |
| Fit | Connects to your work? | 1-5 |
| Urgency | Is someone else about to publish? | 1-5 |

> A score of 3.0 means **adequate**, not good. Be honest.

### Quick Start

```
1. Put your collected papers into 📚 05-文献库/ (one .md per paper)

2. Tell your AI: "Initialize the IDEA system"
   → AI scans your papers, extracts directions, fills 索引.md

3. Generate ideas (choose one):
   a) "Think of new ideas for [your topic]"
      → AI uses 6 methods from 想点子指南.md
   b) Write your own idea into 待评估点子.md
   → Either way, idea gets registered in 索引.md as "待评估"

4. "Evaluate: [idea name]"
   → AI researches + uses template → writes white paper → updates 索引.md
```

### Folder Layout

```
IDEA/
├── 01-灵感收集/     # Ideas (generate)
│   ├── 索引.md       # Central register + novelty map
│   ├── 想点子指南.md  # 6 methods (extensible)
│   └── 待评估点子.md  # Raw pool
├── 02-评估中/       # Evaluation white papers
├── 03-进行中/       # Active projects
├── 04-已归档/       # Done / abandoned
├── 05-文献库/       # Literature (novelty baseline)
└── README.md
```

---

## 中文

### 痛点

| 多数人怎么想点子 | 结果 |
|-----------------|------|
| 等灵感、聊闲天、导师说"试试这个" | **重复造轮子** — 查文献发现别人发过了 |
| 第一个"有意思"的就扎进去 | **选择偏差** — 没有客观比较 |
| 没有系统探索方法 | **方向盲区** — 整个方向都被错过 |

### 工作流

```
1️⃣  你把自己收集的文献放入 📚 05-文献库/（一篇一个 .md）

2️⃣  AI 初始化 → 逐篇读取，抽取研究方向
     ↓
     📋 索引.md 填入：已有方向 + 空白（你的目标区域）

3️⃣  产生点子（两条路）：
     ┌────────────────────────────────────────────┐
     │  A) 让 AI 生成："为 [方向] 想新点子"        │
     │     → AI 按想点子指南.md 的 6 种方法发散     │
     │     → 写入 待评估点子.md                    │
     │     → 登记到 索引.md（状态：待评估）          │
     ├────────────────────────────────────────────┤
     │  B) 自己写点子                              │
     │     → 直接写进 待评估点子.md                 │
     │     → AI 自动同步到 索引.md                 │
     └────────────────────────────────────────────┘

4️⃣  评估："评估：[点子名]"
     → AI 调研 + 按评估模板写白皮书
     → 放入 02-评估中/ 文件夹
     → 更新 索引.md（状态：评估中，填入评分）
```

> **不知道已有啥，就没法判断啥是新的。**

### 快速开始

```
1. 把你看过的文献放进 📚 05-文献库/（一篇一个 .md）
2. "初始化 IDEA 系统"
   → AI 扫描文献，抽取方向，填充 索引.md
3. 产生点子（二选一）：
   a) "为 [方向] 想新点子" → AI 用 6 种方法生成
   b) 自己写点子到 待评估点子.md
   → 无论哪种，点子都会登记到 索引.md（状态：待评估）
4. "评估：[点子名]"
   → AI 调研 + 评估模板 → 白皮书 → 更新 索引.md
```

### 结构

```
IDEA/
├── 01-灵感收集/     生成 → 索引.md 登记（待评估）
├── 02-评估中/       评估 → 索引.md 更新（评分 + 进行中）
├── 03-进行中/       执行
├── 04-已归档/       完成 / 放弃
├── 05-文献库/       文献基线（新颖性依据）
└── README.md
```

---

## License

MIT
