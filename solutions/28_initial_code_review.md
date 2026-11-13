# 28. 找出字符串中第一个匹配项的下标：初始代码复盘

## 一、初始代码

```python
class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack) - len(needle)
        s = len(needle)
        for i in  range(n+1):
            k = i
            m = 0
            while(haystack[k] == needle[k%s]):
                k+=1
                m+=1
            if m >=len(needle):
                return i
            else:
                return -1
```

> 这段代码能通过题目给出的两个示例，但存在多处逻辑错误。在更多用例上会返回错误答案、抛出 `IndexError` 或返回 `None`。

我实际运行验证过：

| `haystack` | `needle` | 期望输出 | 实际结果 |
| :--- | :--- | :---: | :--- |
| `"sadbutsad"` | `"sad"` | `0` | `0` ✅ |
| `"leetcode"` | `"leeto"` | `-1` | `-1` ✅（原因见问题 1） |
| `"ababc"` | `"abc"` | `2` | `-1` ❌ |
| `"aaaa"` | `"aa"` | `0` | `IndexError` ❌ |
| `"a"` | `"a"` | `0` | `IndexError` ❌ |
| `"ab"` | `"abc"` | `-1` | `None` ❌ |

## 二、逻辑错误分析

### 1. `return -1` 写在了循环里面

```python
for i in range(n+1):
    ...
    if m >= len(needle):
        return i
    else:
        return -1   # ← 问题所在
```

`if` 和 `else` 两个分支都有 `return`，意味着**循环第一轮（i = 0）就必定返回**，后面所有起点根本不会被检查。`-1` 表示"所有起点都不匹配"，只能在 `for` 循环**结束后**返回。

以 `haystack = "ababc"`、`needle = "abc"` 为例：i = 0 时前两个字符匹配，第三个字符 `'a' != 'c'`，代码直接 `return -1`，而答案在下标 2。

### 2. `needle[k % s]` 索引写错

`k` 是从 `i` 开始走的指针，但 needle 应该**从下标 0 开始比**，正确的 needle 索引是 `k - i`（或另设一个从 0 开始的指针 `j`）。`k % s` 有两层错误：

- `i > 0` 时从 needle 中间开始比。例如 `i = 1, s = 3` 时会先比 `needle[1]` 而不是 `needle[0]`；
- `k` 超过 `s` 后会对 needle "绕圈"反复比较，没有意义。

这个错误目前被问题 1 掩盖了（因为永远只测 i = 0）。如果只修复问题 1，例如 `haystack = "zzabc"`、`needle = "abc"`，起点依次用 `needle[1]`、`needle[2]` 去比，永远无法匹配，最终错误返回 `-1`。

### 3. `while` 没有终止条件，会越界

```python
while(haystack[k] == needle[k%s]):
```

循环只以"字符不相等"为退出条件，缺少两个限制：

- **已匹配完整串也不停**：`haystack = "aaaa", needle = "aa"` 时 k 一直加，直到 `haystack[4]` 抛出 `IndexError`；
- **匹配到 haystack 末尾也不停**：因此连 `haystack = "a", needle = "a"` 这种最简单、完全匹配的用例都会崩溃。

正确写法是同时限制 needle 指针：`while j < s and ...`。

### 4. needle 比 haystack 长时返回 `None`

`n = len(haystack) - len(needle)` 为负数时，`range(n + 1)` 是空循环，函数一个 `return` 都没执行，最终返回 `None` 而不是 `-1`。把 `return -1` 移到循环外即可顺带解决。

### 5. 变量命名容易混淆

- `n` 实际是"起点个数减一"，`s` 是 needle 长度，`m` 是匹配长度——三个变量含义各不相同却都很短，容易写错；
- needle 上的指针最好单独用 `j` 从 0 开始，不要把 haystack 上的 `k` 和 needle 上的索引混在一起。

## 三、最小修改版

保留原来的双层循环思路，只修上述几点：

```python
class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack) - len(needle)
        s = len(needle)
        for i in range(n + 1):
            k = i      # haystack 上的指针
            j = 0      # needle 上的指针，从 0 开始
            while j < s and haystack[k] == needle[j]:
                k += 1
                j += 1
            if j == s:
                return i
        return -1
```

关键点：

1. `j` 从 0 开始，匹配的 needle 索引是 `j`，而不是 `k % s`；
2. `while` 条件加上 `j < s`，匹配完整串立即停止，也保证 `haystack[k]` 不会越界；
3. `return -1` 移到循环外；
4. `j` 本身充当了匹配长度，不需要额外的 `m`。

- 时间复杂度：`O(m · n)`
- 空间复杂度：`O(1)`

这段代码我已在 10 万组随机用例上与 `str.find` 对拍验证，结果全部一致。

## 四、KMP 算法详解

这道题是 KMP 算法的经典题目。下面从"为什么需要 KMP"讲到完整实现。

### 1. 暴力匹配慢在哪

暴力法失配时，**主串指针要回退**重新比较。最坏情况如 `haystack = "aaaa...aaab"`、`needle = "aaab"`，每个起点都要重比几乎整个 needle，复杂度 `O(m · n)`。

但其实回退后的比较是**大量重复劳动**：失配前已经匹配的那段文本 `haystack[i-j .. i-1]` 等于 `needle[0 .. j-1]`，这段信息完全可以复用——而它只和 needle 自身有关，所以可以事先对 needle 做预处理。

### 2. 核心思想：主串指针永不回退

假设当前已经匹配了 needle 的前 j 个字符，即：

```text
haystack:  ...  x0 x1 ... x(j-1)  c  ...
needle:         p0 p1 ... p(j-1)  pj
                                  ↑ 在这里失配
```

此时 `x0..x(j-1) == p0..p(j-1)`。如果 needle 的前缀 `p0..p(k-1)` 恰好等于这段已匹配文本的后缀 `x(j-k)..x(j-1)`，那么把 needle 右移，让这个前缀对齐到那个后缀，就可以**跳过**这 k 个字符，直接从 `needle[k]` 和 `haystack[i]` 继续比——主串指针 `i` 一步都不用退。

这个 k，就是 `needle[0..j-1]` 的**最长相等真前后缀**（border）的长度。"真前后缀"指不能取整个串本身。

### 3. next（前缀函数）数组

定义：`nxt[i]` = 子串 `needle[0..i]` 的最长相等真前后缀长度。

以 `needle = "aabaaf"` 为例：

| i | needle[0..i] | 最长相等真前后缀 | nxt[i] |
| :---: | :--- | :--- | :---: |
| 0 | `a` | 无 | 0 |
| 1 | `aa` | `a` | 1 |
| 2 | `aab` | 无 | 0 |
| 3 | `aaba` | `a` | 1 |
| 4 | `aabaa` | `aa` | 2 |
| 5 | `aabaaf` | 无 | 0 |

得 `nxt = [0, 1, 0, 1, 2, 0]`。

**构建 next 的过程本身就是一次"自己匹配自己"**。用 `j` 表示"上一个位置的最长 border 长度"，对每个 `i`：

- `needle[i] == needle[j]` → 前后缀可以延长，`j += 1`；
- 不相等 → `j` 回退到 `nxt[j-1]`，直到能继续延长或 `j == 0`。

```python
def build_next(p):
    m = len(p)
    nxt = [0] * m
    j = 0                       # j = p[:i] 的最长 border 长度
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = nxt[j - 1]      # 失配：退到次长的 border
        if p[i] == p[j]:
            j += 1
        nxt[i] = j
    return nxt
```

### 4. 匹配过程

```python
def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    nxt = build_next(needle)

    j = 0                       # needle 上已匹配的长度
    for i in range(n):          # i 只前进，永不回退
        while j > 0 and haystack[i] != needle[j]:
            j = nxt[j - 1]      # 失配：只回退 needle 指针
        if haystack[i] == needle[j]:
            j += 1
        if j == m:
            return i - m + 1    # 全部匹配，返回起点

    return -1
```

拿 `haystack = "aabaabaaf"`、`needle = "aabaaf"`（`nxt = [0,1,0,1,2,0]`）走一遍：

| i | haystack[i] | 与 needle[j] 比较 | 结果 |
| :---: | :---: | :--- | :--- |
| 0 | `a` | `needle[0]=a` | j=1 |
| 1 | `a` | `needle[1]=a` | j=2 |
| 2 | `b` | `needle[2]=b` | j=3 |
| 3 | `a` | `needle[3]=a` | j=4 |
| 4 | `a` | `needle[4]=a` | j=5 |
| 5 | `b` | `needle[5]=f` 失配 | `j = nxt[4] = 2`，再比 `needle[2]=b` 匹配 → j=3 |
| 6 | `a` | `needle[3]=a` | j=4 |
| 7 | `a` | `needle[4]=a` | j=5 |
| 8 | `f` | `needle[5]=f` | j=6=m，返回 `8-6+1 = 3` |

第 5 步是关键：已匹配的 `"aabaa"` 的最长 border 是 `"aa"`（长度 2），它同时是 needle 的前缀和已匹配文本的后缀，所以 needle 相当于右移 3 位，`i = 5` 的字符只需和 `needle[2]` 比，**不用回头重比前两个 `a`**。

### 5. 复杂度为什么是 O(m + n)

以匹配为例：`j` 每次循环最多加 1，所以整个过程中 `j` **总共增加不超过 n 次**；而每次 `while` 回退都会让 `j` 严格变小。因此 `while` 的总执行次数不超过 n 次。主循环 `O(n)`，构建 next 同理 `O(m)`，总计 `O(m + n)`，空间 `O(m)`。

### 6. 和初始代码的关系

初始代码的骨架其实已经对了：一个指针走主串、一个走 needle。KMP 的改动只有两点：

1. needle 指针用独立的 `j` 从 0 开始（不是 `k % s`）；
2. **失配时不把 `i` 退回到下一个起点**，而是让 `j` 跳到 `nxt[j-1]` 继续比。

可以这样理解：**暴力匹配 + "失配时只回退 needle 指针到最长 border" = KMP**。

## 五、KMP 完整可提交版本

```python
class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        # 构建 next（前缀函数）数组
        nxt = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = nxt[j - 1]
            if needle[i] == needle[j]:
                j += 1
            nxt[i] = j

        # 匹配，主串指针 i 不回退
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = nxt[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1

        return -1
```

易错点：

- 回退用 `nxt[j - 1]` 而不是 `nxt[j]`：`nxt[j-1]` 对应"已匹配的那 j 个字符"的最长 border，`nxt[j]` 包含的是没匹配上的当前字符；
- 构建 next 时从 `i = 1` 开始，`nxt[0] = 0` 天然成立；
- 网上很多教程的 next 数组是 `[-1, 0, 1, ...]` 的形式，那只是把本文的数组整体右移一位，思想完全相同。

### 各类方法对比

| 方法 | 时间复杂度 | 空间复杂度 | 说明 |
| :--- | :---: | :---: | :--- |
| 暴力匹配 | `O(m · n)` | `O(1)` | 思路最直接，最坏情况慢 |
| KMP | `O(m + n)` | `O(m)` | 本题的算法考点，主串指针不回退 |
| Python 内置 `haystack.find(needle)` | 线性级别 | 视实现而定 | CPython 用 Two-Way 算法，实际可用，但面试要求手写 |

## 六、本题需要记住的点

1. `return -1` 表示"所有起点都试过了仍不匹配"，必须放在循环**结束后**，不能放进循环的任何分支。
2. 写 `while` 之前先想清楚**终止条件**：比较指针不能越界，目标达成时要能退出。本题的双指针要同时限制 needle 的指针。
3. 比较"某个起点开始的子串"时，needle 的索引应从 0 开始，即 `haystack[i + j] == needle[j]`；不要用 `k % s` 这类取模来"复用"指针。
4. 边界用例必须覆盖：完全匹配、匹配在末尾、needle 与 haystack 等长、needle 更长、大量重复字符（如 `"aaaa"` / `"aa"`）、无匹配。
5. KMP 的核心：`nxt[i]` 是 `needle[0..i]` 的最长相等真前后缀长度；失配时 `j = nxt[j-1]`，主串指针永不回退。
6. KMP 总复杂度 `O(m + n)`：`j` 总共最多增加 n 次，每次回退严格减小 `j`，所以回退总次数也受增加次数约束（摊还分析）。
7. 测试时用随机数据与暴力解/内置 `find` 对拍，是验证字符串匹配类代码最有效的方法。
