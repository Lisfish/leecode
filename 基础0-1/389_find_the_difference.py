"""
389. 找不同
https://leetcode.cn/problems/find-the-difference/

思路：
t 由 s 重排后添加一个字母得到，所以两个字符串只相差那一个字母。
把两个字符串所有字符的 ASCII 码分别求和，t 的总和减去 s 的总和，
差值就是被添加字母的 ASCII 码，再用 chr() 转回字符。

时间复杂度：O(m + n)
空间复杂度：O(1)

另一种常见写法是对所有字符做异或，成对出现的字符会相互抵消，
最后剩下的就是被添加的字母。
"""


class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abcd", "abcde", "e"),
        ("", "y", "y"),
        ("a", "aa", "a"),
        ("ae", "aea", "a"),
    ]

    for s, t, expected in test_cases:
        actual = solution.findTheDifference(s, t)
        assert actual == expected, (
            f"findTheDifference({s!r}, {t!r}) = {actual!r}, "
            f"expected {expected!r}"
        )
        print(f"{s!r} + extra letter -> {t!r} -> {actual!r}")

    print("All tests passed.")
