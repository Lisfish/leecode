"""
28. 找出字符串中第一个匹配项的下标
https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/

思路：
暴力匹配。枚举 haystack 中所有可能的起点 i（0 到 len(haystack) - len(needle)），
逐字符比较 haystack[i:i + len(needle)] 与 needle，第一个完全匹配的 i 即为答案。
如果 needle 比 haystack 长，起点范围为空，直接返回 -1。

时间复杂度：O(m * n)，m、n 分别为 haystack 和 needle 的长度
空间复杂度：O(1)（切片比较会临时占用 O(n)）

另一种更优的写法是 KMP 算法：先对 needle 预处理出 next 数组（最长相同前后缀），
匹配失败时将 needle 的指针回退到 next 位置而不是回退到开头，
时间复杂度可降到 O(m + n)。
"""
