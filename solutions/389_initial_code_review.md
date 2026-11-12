# 389. 找不同：初始代码复盘

## 一、初始代码

```python
class Solution(object):
    def findTheDifference(self, s, t):
        count_s  = {}
        count_t = {}
        for ch in s:
            count_s[ch] = count_s.get(ch,0)+1
        for ch in t:
            count_s[ch] = count_s.get(ch,0)+1
        for ch in t:
            if count_s["ch"] != count_t["ch"]
            return ch
```

> 这段代码目前不能直接运行。整体思路是正确的：分别统计两个字符串中每个字符的出现次数，再比较计数，找出多出来的那个字母。但代码中混入了几处语法错误和逻辑错误。

## 二、语法错误（导致代码无法运行）

| 行号 | 原代码 | 错误原因 | 正确写法 |
| :---: | :--- | :--- | :--- |
| 10 | `if count_s["ch"] != count_t["ch"]` | `if` 语句末尾缺少冒号，Python 通过冒号开始代码块 | `if count_s[ch] != count_t[ch]:` |
| 11 | `return ch` | `if` 下面没有缩进，Python 会报 `IndentationError`，代码块的范围由缩进决定 | 缩进到 `if` 块内部 |

### 相关 Python 基础

```python
# if 语句用冒号开始代码块，块的范围靠缩进划分
if 条件:
    代码

# 带引号的是字符串字面量，不带引号的是变量
ch = "a"
"ch"    # 由 c、h 两个字符组成的字符串，和变量 ch 没有任何关系
```

## 三、逻辑错误（语法修好后仍会出错）

### 1. 第二个循环统计进了错误的字典

原代码第 8 行：

```python
count_s[ch] = count_s.get(ch, 0) + 1
```

这里本应统计 `t` 的字符，却把结果写进了 `count_s`。结果是 `count_s` 变成了两个字符串的合并计数，而 `count_t` 始终是空字典，后面的比较无法得到正确结果。

正确写法：

```python
count_t[ch] = count_t.get(ch, 0) + 1
```

> 这是复制上一段循环后忘记修改变量名的典型错误。复制粘贴后要逐字检查被复制的每一处变量名。

### 2. `"ch"` 是字符串，不是变量 `ch`

原代码第 10 行：

```python
if count_s["ch"] != count_t["ch"]
```

`"ch"` 是一个由 `c`、`h` 两个字符组成的字符串字面量，而不是循环变量 `ch`。字典中只存在单个字符的键，因此取 `count_s["ch"]` 会直接抛出 `KeyError: 'ch'`。

正确写法：

```python
if count_s[ch] != count_t[ch]:
```

### 3. 缺键时用下标访问会抛 `KeyError`

修正以上两处后，代码在 `s = "abcd", t = "abcde"` 上仍然会崩溃：

```text
KeyError: 'e'
```

原因是 `count_s` 中并不存在键 `'e'`，执行 `count_s['e']` 时抛出了异常。被添加的字母可能从未在 `s` 中出现过（`s = ""` 时必然如此），所以访问 `count_s` 时必须用 `get` 提供默认值：

```python
count_s.get(ch, 0)
```

`count_s.get(ch, 0)` 的含义是：键 `ch` 存在时返回它的计数，不存在时返回 `0`，从而避免 `KeyError`。

`count_t[ch]` 则不需要修改，因为循环遍历的就是 `t` 的字符，该键一定存在。

## 四、最小修改版

```python
class Solution(object):
    def findTheDifference(self, s, t):
        count_s = {}
        count_t = {}
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        for ch in t:
            if count_s.get(ch, 0) != count_t.get(ch, 0):
                return ch
```

验证用例：

| `s` | `t` | 输出 | 说明 |
| :--- | :--- | :---: | :--- |
| `"abcd"` | `"abcde"` | `"e"` | 新增字符是全新字母，能暴露缺键问题 |
| `""` | `"y"` | `"y"` | `s` 为空，`t` 的字符全部不在 `count_s` 中 |
| `"ae"` | `"aea"` | `"a"` | 新增字符与已有字符重复，不能用「是否存在」判断 |

## 五、可改进之处

### 1. 只需要一个字典

`count_s` 统计完成后，遍历 `t` 逐个「消耗」计数即可，不需要再建 `count_t`：

```python
class Solution(object):
    def findTheDifference(self, s, t):
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in t:
            if counts.get(ch, 0) == 0:
                return ch
            counts[ch] -= 1
```

少遍历一次字符串，也不用处理两侧缺键，是这道题更常见的写法。

### 2. 利用题目结构的 O(1) 空间写法

题目保证 `t` 只比 `s` 多一个字母，因此还可以用 ASCII 码求和或异或：

```python
# 求和方法
return chr(sum(map(ord, t)) - sum(map(ord, s)))
```

```python
# 异或方法：成对出现的字符相互抵消
result = 0
for ch in s + t:
    result ^= ord(ch)
return chr(result)
```

| 方法 | 时间复杂度 | 空间复杂度 | 特点 |
| :--- | :---: | :---: | :--- |
| 字典计数 | `O(m + n)` | `O(k)`，`k` 为不同字符数（≤26） | 最通用，题目条件变化时依然成立 |
| ASCII 求和 | `O(m + n)` | `O(1)` | 代码最短，依赖「只多一个字符」 |
| 异或 | `O(m + n)` | `O(1)` | 技巧性强，可复用到第 136 题 |

## 六、本题需要记住的点

1. `dict.get(key, default)` 在键不存在时返回默认值，是计数字典的标准写法，能避免 `KeyError`。
2. 带引号的 `"ch"` 是字符串字面量，不带引号的 `ch` 才是变量，二者完全不同。
3. `if` 和 `for` 语句末尾要写冒号，代码块的范围由缩进决定。
4. 复制粘贴代码后，务必检查每一处变量名是否都要修改（本题的 `count_s` / `count_t`）。
5. 测试用例要覆盖边界：`s` 为空、新增字符从未在 `s` 中出现、新增字符与已有字符重复。
6. 「分别计数再比较」通用性最好；求和、异或更简洁，但依赖题目「只多一个字符」的特殊结构。
