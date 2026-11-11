"""
1768. 交替合并字符串
https://leetcode.cn/problems/merge-strings-alternately/

思路：
按下标 i 同时遍历两个字符串，循环次数取两者长度的较大值。
每一轮中，只要 i 没有超出某个字符串的长度，就取其对应字符加入结果。
这样较短的字符串遍历完后，较长的字符串剩余部分会自动追加到末尾。

时间复杂度：O(m + n)
空间复杂度：O(m + n)
"""


class Solution(object):
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])

        return "".join(merged)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
    ]

    for word1, word2, expected in test_cases:
        actual = solution.mergeAlternately(word1, word2)
        assert actual == expected, (
            f"mergeAlternately({word1!r}, {word2!r}) = {actual!r}, "
            f"expected {expected!r}"
        )
        print(f"{word1!r} + {word2!r} -> {actual!r}")

    print("All tests passed.")
