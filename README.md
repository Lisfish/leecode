<div align="center">

# LeetCode · Python 刷题记录

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Practice-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.cn/)
![Status](https://img.shields.io/badge/Status-In%20Progress-2575FC?style=flat-square)

记录我使用 Python 练习 LeetCode 的题解与思路。后续题目会按阶段或专题放入不同文件夹，并持续更新。


</div>

## 📖 项目简介

- **语言**：Python 3.10+
- **内容**：每题包含思路说明、代码实现、复杂度分析
- **组织方式**：按阶段或专题划分文件夹，便于持续练习和复习
- **依赖**：无第三方依赖，标准库即可运行

## 📂 目录结构

```text
leecode/
├── README.md
├── .gitignore
├── 基础0-1/
│   ├── 1768_initial_code_review.md
│   └── 1768_merge_strings_alternately.py
├── git使用介绍/
│   └── README.md
└── solutions/
    └── .gitkeep
```

后续刷题安排：

- `基础0-1/`：基础阶段练习目录，用于记录接下来的 LeetCode 入门题目。
- `solutions/`：预留的 Hot 100 题解目录，后续可按分类继续补充。

命名规则：`题号_英文题名.py`，题号补足三位，题名用 snake_case。
例如 LeetCode 1「两数之和」→ `001_two_sum.py`。

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

每个题解文件使用统一结构，方便复习：

```python
"""
1. 两数之和
https://leetcode.cn/problems/two-sum/

思路：用哈希表记录已经遍历过的元素，查找 target - num 是否出现过。
时间复杂度：O(n)
空间复杂度：O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        return []
```

## ▶️ 运行方式

```bash
python solutions/001_two_sum.py
```

建议在文件末尾用 `if __name__ == "__main__":` 写几组测试用例，方便本地自测。



## 🔗 参考

- [LeetCode 热题 100](https://leetcode.cn/studyplan/top-100-liked/)
- [Python 官方文档](https://docs.python.org/3/)

---

如果这些题解对你有帮助，欢迎 Star ⭐；有更好的写法也欢迎交流。
