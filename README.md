<div align="center">

# LeetCode · Python 刷题记录

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Practice-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.cn/)
![Status](https://img.shields.io/badge/Status-In%20Progress-2575FC?style=flat-square)

记录我使用 Python 练习 LeetCode 的题解与思路。后续题目会按阶段或专题放入不同文件夹，并持续更新。


</div>

## 📖 项目简介

- **语言**：Python 3.10+
- **内容**：`基础0-1/` 记录题目、解题思路与复杂度分析；`solutions/` 保存初始代码复盘，包含错误分析、修正代码与算法详解
- **组织方式**：按阶段或专题划分文件夹，便于持续练习和复习
- **依赖**：无第三方依赖，标准库即可运行

## 📂 目录结构

```text
leecode/
├── README.md
├── .gitignore
├── 基础0-1/
│   ├── 28_find_the_index_of_the_first_occurrence_in_a_string.py
│   ├── 389_find_the_difference.py
│   └── 1768_merge_strings_alternately.py
├── git使用介绍/
│   └── README.md
└── solutions/
    ├── 28_initial_code_review.md
    ├── 389_initial_code_review.md
    └── 1768_initial_code_review.md
```

后续刷题安排：

- `基础0-1/`：基础阶段练习目录，仅保留题目、思路和复杂度分析，不放置代码，代码独立练习后记录在复盘文档中。
- `solutions/`：初始代码复盘目录，按题号记录初版代码的错误分析与改进过程，后续可按分类继续补充。

命名规则：`题号_英文题名.py`，题号按题目原编号书写（不补零），题名用 snake_case。
例如 LeetCode 28「找出字符串中第一个匹配项的下标」→ `28_find_the_index_of_the_first_occurrence_in_a_string.py`。

## ✅ 已完成题目

| 题号 | 题目 | 核心思路 | 复盘 |
| :---: | :--- | :--- | :---: |
| 28 | [找出字符串中第一个匹配项的下标](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 暴力匹配；KMP 失配时按 next 数组回退 | [复盘](solutions/28_initial_code_review.md) |
| 389 | [找不同](https://leetcode.cn/problems/find-the-difference/) | ASCII 求和 / 异或 | [复盘](solutions/389_initial_code_review.md) |
| 1768 | [交替合并字符串](https://leetcode.cn/problems/merge-strings-alternately/) | 双指针按下标交替拼接 | [复盘](solutions/1768_initial_code_review.md) |

## 📚 学习资料

- [Git 使用指南](git使用介绍/README.md)

## 📊 Hot 100 刷题进度

| 分类 | 题数 | 进度 |
| :--- | :---: | :---: |
| 哈希 | 3 | 0 / 3 |
| 双指针 | 4 | 0 / 4 |
| 滑动窗口 | 2 | 0 / 2 |
| 子串 | 3 | 0 / 3 |
| 普通数组 | 5 | 0 / 5 |
| 矩阵 | 4 | 0 / 4 |
| 链表 | 14 | 0 / 14 |
| 二叉树 | 15 | 0 / 15 |
| 图论 | 4 | 0 / 4 |
| 回溯 | 8 | 0 / 8 |
| 二分查找 | 6 | 0 / 6 |
| 栈 | 5 | 0 / 5 |
| 堆 | 3 | 0 / 3 |
| 贪心算法 | 4 | 0 / 4 |
| 动态规划 | 10 | 0 / 10 |
| 多维动态规划 | 5 | 0 / 5 |
| 技巧 | 5 | 0 / 5 |
| **合计** | **100** | **0 / 100** |

> 每完成一题，更新对应分类的进度，并在文件内写清思路与复杂度。

## 🗂️ 题解模板

`基础0-1/` 中的文件只记录题目与思路，不包含代码：

```python
"""
28. 找出字符串中第一个匹配项的下标
https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/

思路：暴力匹配。枚举所有可能的起点，逐字符与 needle 比较；
全部起点尝试完仍未匹配则返回 -1。

时间复杂度：O(m * n)
空间复杂度：O(1)
"""
```

初始代码、错误分析与修正版本统一记录在 `solutions/<题号>_initial_code_review.md`。

## ▶️ 本地验证

复习时，将 `solutions/` 复盘文档中的完整代码复制到本地 `.py` 文件运行，即可验证思路。

## 🔗 参考

- [LeetCode 热题 100](https://leetcode.cn/studyplan/top-100-liked/)
- [Python 官方文档](https://docs.python.org/3/)

---

如果这些题解对你有帮助，欢迎 Star ⭐；有更好的写法也欢迎交流。
