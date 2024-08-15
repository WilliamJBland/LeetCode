"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
 "abcde" while "aec" is not).

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_pointer, full_pointer = 0, 0
        while full_pointer < len(t) and sub_pointer < len(s):
            if s[sub_pointer] == t[full_pointer]:
                sub_pointer += 1
            full_pointer += 1
        return True if sub_pointer == len(s) else False



if __name__ == '__main__':
    s = 'oohello'
    t = 'opophpeplplpop'
    res = Solution().isSubsequence(s, t)
    print(res)

