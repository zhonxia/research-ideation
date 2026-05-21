# Idea Lab

[English](#english) | [中文](#中文)

---

## English

### What is this?

A structured system for **generating, evaluating, and managing research ideas**. Built as a WorkBuddy skill, it helps academic researchers systematically explore research directions instead of waiting for inspiration.

### Who is it for?

Researchers in AI/ML, data science, engineering, or any field where you need to:
- Generate novel research directions
- Evaluate whether an idea is worth pursuing
- Track and compare multiple ideas
- Verify novelty against existing literature

### How does it work?

The system provides **6 structured brainstorming methods**:

| Method | What it does |
|--------|-------------|
| **Combination Innovation** | Pair your method with new technologies or domains |
| **Fix Weaknesses** | Mine "limitations" sections from papers for unsolved problems |
| **Transplant Methods** | Import mature theories from other fields |
| **Theory Deep Dive** | Find unproven properties and relaxed boundary conditions |
| **Boundary Limits** | Challenge default assumptions in existing research |
| **Literature Deconstruction** | Extract "Future Work" gaps from top papers |

Each idea gets evaluated on 6 dimensions (novelty, feasibility, verifiability, publishability, fit, urgency) and scored 0-30.

### Quick Start

1. Install the skill in WorkBuddy
2. Create an `IDEA/` folder in your workspace
3. Tell WorkBuddy: "Initialize the IDEA folder structure"
4. Start generating: "Think of new ideas for [your research topic]"
5. Evaluate: "Evaluate: [idea name]"

### Folder Structure

```
IDEA/
├── 01-灵感收集/          # Idea collection
│   ├── 索引.md            # Index + novelty map
│   ├── 想点子指南.md       # How to generate ideas
│   └── 待评估点子.md       # Raw brainstorming pool
├── 02-评估中/            # Under evaluation
│   └── [idea-name]/
│       └── [evaluation].md
├── 03-进行中/            # Actively working
├── 04-已归档/            # Done or abandoned
└── README.md
```

---

## 中文

### 这是什么？

一个**系统化生成、评估和管理研究点子**的工作流。作为 WorkBuddy 技能，帮助研究者用结构化方法探索研究方向，而不是等灵感降临。

### 适合谁？

AI/ML、数据科学、工程等领域的研究者，尤其是需要：
- 系统化生成新颖的研究方向
- 客观点子是否值得推进
- 跟踪和比较多点子
- 对照已有文献验证新颖性

### 怎么用？

系统提供 **6 种结构化发散方法**：

| 方法 | 作用 |
|------|------|
| **组合创新** | 你的方法 + 新技术/新场景 |
| **补短板** | 从论文的"局限性"中挖未解决的问题 |
| **搬方法** | 从其他领域移植成熟理论 |
| **理论深挖** | 找未被证明的数学性质 |
| **边界极限法** | 挑战现有研究的默认假设 |
| **文献解构法** | 从顶级论文的"Future Work"中挖坑 |

每个点子按 6 个维度打分（新颖性、可行性、可验证性、发表性、契合度、紧迫性），满分 30。

### 快速开始

1. 在 WorkBuddy 中安装此技能
2. 在工作区创建 `IDEA/` 文件夹
3. 告诉 WorkBuddy：「初始化 IDEA 文件夹结构」
4. 开始发散：「为 [你的研究方向] 想新点子」
5. 评估点子：「评估：[点子名]」

### 文件结构

```
IDEA/
├── 01-灵感收集/          # 灵感收集
│   ├── 索引.md            # 索引 + 新颖性验证
│   ├── 想点子指南.md       # 想点子方法论
│   └── 待评估点子.md       # 碎片想法收集池
├── 02-评估中/            # 评估中
│   └── [点子名]/
│       └── [评估白皮书].md
├── 03-进行中/            # 进行中
├── 04-已归档/            # 已归档
└── README.md
```

---

## License

MIT
