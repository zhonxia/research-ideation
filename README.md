# Research Ideation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/zhonxia/research-ideation/blob/main/LICENSE)

> **Stop waiting for inspiration. Start generating ideas systematically.**
> 文献库是你的新颖性基线。AI 负责穷举、评分、管理，你只负责判断。

[English](#english) · [中文](#中文)

---

## English

### The Problem & Fix

| How most researchers do it | What goes wrong | How this fixes it |
|---------------------------|-----------------|-------------------|
| Random inspiration, hallway chats, advisor says "try this" | **Duplication** — spend weeks, find out it's already published | 📚 Literature scan → index marks existing directions, collision visible instantly |
| Jump on the first "interesting" idea | **Selection bias** — no objective comparison | 📊 6-dimension 30-pt scoring → compare all ideas side by side |
| No systematic exploration method | **Blind spots** — miss entire research directions | 💡 6 structured brainstorming methods → explore every corner of the space |

### Traditional vs This Skill

| Traditional | → | This Skill |
|------------|---|------------|
| "Is this novel? Not sure..." | → | Literature scan reveals what exists + where the gaps are |
| "I only have 1-2 ideas" | → | 6 methods generate diverse candidates, scored objectively |
| "This one feels right, let's go" | → | Compare all candidates, pick the highest score |
| "What happened to that idea from last year?" | → | Index tracks full lifecycle: 待评估→评估中→进行中→已归档 |

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

| Step | What to do | Say / Action |
|------|-----------|--------------|
| 1 | Drop papers into 📚 05-文献库/ | Manually, one .md per paper |
| 2 | AI scans papers, fills index | "Initialize the IDEA system" |
| 3 | Generate ideas (two paths) | "Think of new ideas for [topic]" / Write into 待评估点子.md |
| 4 | Evaluate an idea | "Evaluate: [idea name]" |
| 5 | Track progress | Auto-updated in 索引.md |

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

### 痛点与解法

| 痛点 | 结果 | 本技能怎么解决 |
|------|------|---------------|
| 等灵感、聊闲天、导师说"试试这个" | **重复造轮子** — 查文献发现别人发过了 | 📚 文献库自动扫描 → 索引标出已有方向，撞没撞车一眼知道 |
| 第一个"有意思"的就扎进去 | **选择偏差** — 没有客观比较 | 📊 6 维度 30 分评分 → 所有点子横向对比，数据说了算 |
| 没有系统探索方法 | **方向盲区** — 整个方向都被错过 | 💡 6 种结构化发散方法 → 穷举可能性空间，空白就是目标 |

### 传统方式 vs 本技能

| 传统 | → | 本技能 |
|------|---|--------|
| "这个方向有人做过了吗？不确定..." | → | 文献库一扫描，已有方向 + 空白区域一目了然 |
| "我就 1-2 个想法，不知道好不好" | → | 6 种方法发散 → 覆盖全部可能性 → 30 分客观评分 |
| "先做这个吧，感觉还行" | → | 横向对比所有备选，选分数最高的 |
| "去年那个点子后来怎么样了？" | → | 索引追踪全生命周期：待评估→评估中→进行中→已归档 |

> **不知道已有啥，就没法判断啥是新的。**
> 文献库是你的新颖性基线。每一篇论文都告诉 AI 什么已被探索过，
> 剩下的空白区域，就是你该去的地方。

### 快速开始

| 步骤 | 操作 | 输入 |
|------|------|------|
| 1 | 把文献放进 📚 05-文献库/ | 手动放，一篇一个 .md |
| 2 | AI 扫描文献，填充索引 | "初始化 IDEA 系统" |
| 3 | 产生点子（二选一） | "为 [方向] 想新点子" / 自己写到 待评估点子.md |
| 4 | 评估点子 | "评估：[点子名]" |
| 5 | 追踪进度 | 自动更新 索引.md 状态 |

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
