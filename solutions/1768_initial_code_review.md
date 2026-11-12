# 1768. 交替合并字符串：初始代码复盘

## 一、初始代码

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len_1 = len(word1)
        len_2 = len(word2)
        result = []
        if (len_1>len_2){
            for i in range len_2-1{
                result.append[word1[i]]
                result.append[word2[i]]
            }
            for (i=len_2-1,i<len_1,i++){
                result.append[word1[i]]
            }
        else:{
            for i in range len_1-1{
                result.append[word1[i]]
                result.append[word2[i]]
            }
            for (i=len_1-1,i<len_2,i++){
                result.append[word2[i]]
        }
        return result
        }
```

> 这段代码目前不能直接运行。整体思路是正确的，但混用了 Python 和 C/Java 的语法。

## 二、语法错误（导致代码无法运行）

| 行号 | 原代码 | 错误原因 | 正确写法 |
| :---: | :--- | :--- | :--- |
| 11 | `if (len_1>len_2){` | Python 用冒号开始代码块，不使用 `{}` | `if len_1 > len_2:` |
| 12 | `for i in range len_2-1{` | `range` 是函数，参数必须放在括号中；`{` 也不是 Python 语法 | `for i in range(len_2):` |
| 13 | `result.append[word1[i]]` | `append` 是方法，应该用圆括号调用；方括号表示下标访问 | `result.append(word1[i])` |
| 14 | `result.append[word2[i]]` | 同上 | `result.append(word2[i])` |
| 15、18、23 | `}` | Python 没有用 `{}` 表示代码块，块的范围由缩进决定 | 删除，改为正确缩进 |
| 16 | `for (i=len_2-1,i<len_1,i++){` | Python 不支持 C/Java 的三段式 `for` 循环 | `for i in range(len_2, len_1):` |
| 19 | `else:{` | `else` 后面只能写冒号；并且 `else` 应与 `if` 对齐 | `else:` |
| 20 | `for i in range len_1-1{` | 与第 12 行相同，既缺少函数括号，也使用了错误的花括号 | `for i in range(len_1):` |
| 24 | `for (i=len_1-1,i<len_2,i++){` | 与第 16 行相同，C/Java 循环写法在 Python 中无效 | `for i in range(len_1, len_2):` |
| 26、28 | `}` | Python 中不存在用于结束代码块的花括号 | 删除，依靠缩进组织代码 |

### 相关 Python 基础

```python
# Python 的代码块用冒号和缩进，不用花括号
if 条件:
    代码

# range 是函数，必须加括号
for i in range(10):
    代码

# append 是列表方法，必须用圆括号调用
result.append(值)
```

## 三、逻辑错误（语法修好后仍会出错）

### 1. 公共部分少遍历一位

原代码：

```python
for i in range(len_2 - 1):
```

`range(len_2 - 1)` 生成的是 `0` 到 `len_2 - 2`，会漏掉短字符串的最后一个字符。

正确写法：

```python
for i in range(len_2):
```

### 2. 补尾部时从错误的位置开始

原代码：

```python
for i in range(len_2 - 1, len_1):
```

因为前一个循环已经处理了下标 `len_2 - 1`，这里再次从 `len_2 - 1` 开始会导致最后一个公共字符重复。

正确写法：

```python
for i in range(len_2, len_1):
```

`else` 分支中的 `len_1 - 1` 也有相同问题，应改为：

```python
for i in range(len_1, len_2):
```

### 3. 返回了列表，而不是字符串

原代码：

```python
return result
```

`result` 的类型是 `list`，题目要求返回 `str`。应把列表中的字符连接成字符串：

```python
return "".join(result)
```

## 四、最小修改版


```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len_1 = len(word1)
        len_2 = len(word2)
        result = []

        if len_1 > len_2:
            for i in range(len_2):
                result.append(word1[i])
                result.append(word2[i])

            for i in range(len_2, len_1):
                result.append(word1[i])
        else:
            for i in range(len_1):
                result.append(word1[i])
                result.append(word2[i])

            for i in range(len_1, len_2):
                result.append(word2[i])

        return "".join(result)
```

## 五、可改进之处

上面的两个分支有大量重复代码。可以统一循环到两个字符串中较长的长度，再判断当前下标是否越界：

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])

        return "".join(result)
```

- 时间复杂度：`O(m + n)`
- 空间复杂度：`O(m + n)`

## 六、本题需要记住的点

1. Python 用缩进划分代码块，不写 `{}`。
2. `range(...)` 必须加括号。
3. `append(...)` 是方法调用，必须用圆括号。
4. Python 的 `for` 是“遍历”语义，不写 C/Java 的三段式循环。
5. 使用下标时重点检查边界：起点是否重复、终点是否遗漏。
6. 返回值类型要和题目要求一致，列表转字符串用 `"".join(result)`。
