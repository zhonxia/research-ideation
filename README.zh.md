# Research Ideation v4

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![v4](https://img.shields.io/badge/version-v4-brightgreen)]()

🇬🇧 [English](README.md)

一套基于证据的学术研究点子生成、筛选、评估和管理的系统化工作流。

---

### v4 的核心变化

v4 不再让每个灵感直接进入完整白皮书，而是采用逐级增加成本的漏斗：

```text
Inbox → 去重 → 初筛 → 评估 → 最小可否证探针 → 进行中
                    ↘ 拒绝       ↘ 搁置 / 重复 / 已取代 / 归档
```

主要改进：

- 使用稳定点子 ID：`IDEA-YYYY-NNNN`
- 严格区分"本地文献未覆盖"和"经检索支持的研究缺口"
- 评分前先检查问题重要性、可回答性、资源和伦理四项硬门槛
- 使用带置信度与敏感性分析的百分制评分
- 紧迫性只影响排程，不再抬高质量总分
- 支持理论、计算实验、定性、临床/现场、设计/构造研究
- 十一种互补生成方法，新增矛盾地图、反例先行、测量先行、制度与相图法
- 用问题发现型和方法增益型两条路线系统化组合创新，并共享经核验的跨领域方法库
- 用轻量研究点子卡衔接初筛与正式评估
- 将创新主张拆成四部分，经过宽搜、摘要初筛和重点全文核查后写出明确差异陈述
- `索引.md` 是唯一生命周期真相源，`待评估点子.md` 只做临时 inbox
- 白皮书引用 claim/evidence ID，不复制证据表
- 初始化器确定性映射文件，校验器兼容旧格式

### 初始化

```bash
python scripts/init_idea.py /path/to/IDEA
```

默认不会覆盖已有文件。需要明确替换模板时才使用 `--force`。

初始化器创建的目录结构：

```text
IDEA/
├── 01-灵感收集/
│   ├── 索引.md
│   ├── 想点子指南.md
│   ├── 待评估点子.md
│   ├── _研究点子卡模板.md
│   ├── evidence-log.md
│   └── 问题结构图谱.md
├── 02-评估中/
├── 03-进行中/
├── 04-已归档/
├── 05-文献库/
│   └── _文献模板.md
├── 06-跨领域方法库/
│   ├── 索引.md
│   ├── 扫描记录.md
│   └── 领域/
│       └── _方法卡模板.md
└── README.md
```

### 校验

```bash
python scripts/validate_idea_index.py /path/to/IDEA
python scripts/validate_idea_index.py /path/to/IDEA --strict --require-ids
```

校验器检查：

- ID 唯一性及稳定性
- 状态是否符合规范
- 必填决策字段与分值范围
- 文件夹与注册表一致性
- 白皮书 `idea_id` 元数据
- Evidence/claim ID 及未解析引用
- Inbox 中引用了不存在点子的记录

旧索引仍可读取；旧状态、缺失稳定 ID、标题模糊匹配会给出迁移警告。新建工作区应直接满足 v4 契约。

### 十一种生成方法

1. 组合创新
2. 弱点三角验证
3. 方法移植
4. 理论深挖
5. 边界与假设挑战
6. 引文链缺口挖掘
7. 目标反向推导
8. 矛盾地图
9. 反例先行
10. 测量先行
11. 制度与相图

组合创新不直接做"领域名 × BRB"，而是先选择主要验证路线：

- **问题存在性**：先验证目标问题是否真实且足够严重，再评价解决方案。
- **效果实证**：目标任务本身已经成立，直接检验适配后的成熟方法能否以有意义幅度优于强基线和未经适配的直接移植。

两条路线都检查结构拟合、假设兼容性、本领域替代方案和非平凡改造，并保留负匹配历史。效果实证型必须报告消融、不确定性以及数据、参数、调参、计算和维护成本，不能只报告单一数据集上的平均提升。

### 核心原则

1. 本地库缺失只能说明本地覆盖缺口。
2. 点子离开 inbox 时分配稳定 ID，ID 永不复用。
3. 硬门槛通过后再评分。
4. 分数必须包含证据理由和置信度。
5. 只比较相同评分版本和兼容研究类型。
6. 生命周期、证据或文件夹变化后立即校验。

### 仓库结构

```text
SKILL.md                    核心工作流与路由
agents/openai.yaml          Codex UI 元数据
assets/                     工作区模板
references/                 详细方法与契约
references/cross-domain-method-atlas.md  组合搜索协议
references/validation-routes.md  问题存在性与效果实证验证路线
scripts/init_idea.py        确定性初始化器
scripts/validate_idea_index.py  工作区校验器
scripts/package_skill.py    精简发布包构建器
tests/                      标准库测试套件
```

MIT 许可证。
