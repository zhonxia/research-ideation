# Research Ideation

> A WorkBuddy skill for systematic research idea management.
>
> **Stop waiting for inspiration. Start generating ideas systematically.**

[English](#english) | [中文](#中文)

---

## English

### The Problem

Most researchers generate ideas haphazardly — random inspiration, conference hallway conversations, supervisor suggestions. This leads to:

- **Duplication**: Spending weeks on an idea only to discover it's already been published
- **Bias**: Over-investing in the first idea that seems promising without comparing alternatives
- **Blind spots**: Missing entire research directions because no method exists to systematically explore the space

### The Solution

Research Ideation provides a **structured pipeline** with three layers:

| Layer | What it does | Key artifacts |
|-------|-------------|--------------|
| **Literature Baseline** | Extract research directions from papers you've read → know what already exists | `05-文献库/` → `索引.md` (novelty map + gap analysis) |
| **Idea Generation** | 6 systematic brainstorming methods → cover the full search space | `待评估点子.md` → `索引.md` (register as pending) |
| **Idea Evaluation** | 30-point scoring across 6 dimensions → compare ideas objectively | `02-评估中/` (white paper) → `索引.md` (update status + score) |
| **Lifecycle Tracking** | Track every idea through 待评估 → 评估中 → 进行中 → 已归档 | `索引.md` (single source of truth) |

### The Key Insight

**You can't know what's new until you know what exists.**

The `文献库/` folder builds your novelty baseline. Before generating ideas, the skill scans your literature collection, extracts research directions from each paper, and maps the landscape. This tells you where the gaps are — so every new idea targets unexplored territory.

### 6 Brainstorming Methods

| # | Method | Core Question |
|---|--------|---------------|
| 1 | **Combination Innovation** | What if I combined my method with [new technology] in [new domain]? |
| 2 | **Fix Weaknesses** | What problems do survey papers keep mentioning as "limitations"? |
| 3 | **Transplant Methods** | What mature theory from another field can solve my bottleneck? |
| 4 | **Theory Deep Dive** | What mathematical properties remain unproven? |
| 5 | **Boundary Limits** | What if the default assumptions in my field are wrong? |
| 6 | **Literature Deconstruction** | What "Future Work" gaps did top papers leave unfilled? |

### 6-Dimension Scoring (30 points total)

| Dimension | Question |
|-----------|----------|
| Novelty | Has anyone done this before? |
| Feasibility | Can it actually be built? |
| Verifiability | Can I prove it works? |
| Publishability | Will reviewers buy it? |
| Fit | Does it connect to my existing work? |
| Urgency | Is someone else about to publish this? |

### Folder Structure

```
IDEA/
├── 01-灵感收集/          # Generate
│   ├── 索引.md            # Central registry: all ideas (生命周期: 待评估→评估中→进行中→已归档) + literature novelty map
│   ├── 想点子指南.md       # Brainstorming methodology (extensible)
│   └── 待评估点子.md       # Raw idea pool (pre-evaluation)
├── 02-评估中/            # Evaluate
│   └── [idea-name]/
│       └── [evaluation].md
├── 03-进行中/            # Execute
├── 04-已归档/            # Done / abandoned
├── 05-文献库/            # Literature baseline
│   └── [paper-title].md  # One file per paper: direction + core idea
└── README.md
```

### Quick Start

```bash
# 1. Install the skill in WorkBuddy
# 2. Tell WorkBuddy:
"Initialize the IDEA folder structure"

# 3. Add papers to 05-文献库/ (one .md per paper)

# 4. Re-sync the literature baseline:
"Sync the literature library to the index"

# 5. Generate ideas:
"Think of new ideas for [your research topic]"

# 6. Evaluate an idea:
"Evaluate: [idea name]"

# 7. Compare all ideas:
"Show me the horizontal comparison of all evaluated ideas"
```

---

## 中文

### 痛点

多数研究者靠灵感碰撞想点子——随机、低效、容易踩坑：

- **重复造轮子**：花几周研究，发现已被发表
- **选择偏差**：想到第一个点子就扎进去，没有横向比较
- **方向盲区**：没人帮你系统地穷举可能性空间

### 解决方案

Research Ideation 提供**三层结构化管线**：

| 层 | 做什么 | 核心产物 |
|----|--------|----------|
| **文献基线** | 从已读论文中抽取研究方向 → 知道已有啥 | `05-文献库/` → `索引.md`（新颖性地图 + 空白分析） |
| **点子生成** | 6 种结构化发散方法 → 覆盖搜索空间 | `待评估点子.md` → `索引.md`（登记为待评估） |
| **点子评估** | 6 维度 30 分制评分 → 客观横向比较 | `02-评估中/`（白皮书） → `索引.md`（更新评分+状态） |
| **生命周期追踪** | 追踪每个点子：待评估→评估中→进行中→已归档 | `索引.md`（唯一真相来源） |

### 核心洞见

**不知道已有啥，就没法判断啥是新的。**

`文献库/` 文件夹建立你的新颖性基线。每次初始化或同步时，技能会扫描你的文献库，提取每篇论文的研究方向，绘制出领域地图。地图上的空白，就是你该去的地方。

### 6 种发散方法

| # | 方法 | 核心问题 |
|---|------|----------|
| 1 | **组合创新** | [你的方法] + [新技术] 在 [新场景] 下会怎样？ |
| 2 | **补短板** | 综述论文里反复提到的"limitation"是什么？ |
| 3 | **搬方法** | 别的领域有什么成熟理论能解决你的瓶颈？ |
| 4 | **理论深挖** | 还有哪些数学性质没被证明？ |
| 5 | **边界极限法** | 如果领域里的默认假设是错的呢？ |
| 6 | **文献解构法** | 顶刊论文的 "Future Work" 留了哪些坑？ |

### 6 维度评分（满分 30）

| 维度 | 问题 |
|------|------|
| 新颖性 | 有人做过吗？ |
| 可行性 | 能做出来吗？ |
| 可验证性 | 能证明有效吗？ |
| 发表性 | 审稿人会买账吗？ |
| 契合度 | 跟你已有的工作衔接吗？ |
| 紧迫性 | 别人快发了吗？ |

### 文件夹结构

```
IDEA/
├── 01-灵感收集/          # 生成
│   ├── 索引.md            # 中央登记册：所有点子（待评估→评估中→进行中→已归档）+ 文献新颖性地图
│   ├── 想点子指南.md       # 发散方法论（可扩展）
│   └── 待评估点子.md       # 碎片想法收集池（评估前）
├── 02-评估中/            # 评估
│   └── [点子名]/
│       └── [评估白皮书].md
├── 03-进行中/            # 执行
├── 04-已归档/            # 完成 / 放弃
├── 05-文献库/            # 文献基线
│   └── [论文名].md        # 一篇论文一个文件：方向 + 核心点子
└── README.md
```

### 快速开始

```bash
# 1. 在 WorkBuddy 中安装技能
# 2. 告诉 WorkBuddy：
"初始化 IDEA 文件夹结构"

# 3. 往 05-文献库/ 添加论文（一篇一个 .md）

# 4. 同步文献基线：
"把文献库同步到索引"

# 5. 想点子：
"为 [你的研究方向] 想新点子"

# 6. 评估点子：
"评估：[点子名]"

# 7. 横向比较：
"给我看所有已评估点子的横向对比"
```

---

## License

MIT
