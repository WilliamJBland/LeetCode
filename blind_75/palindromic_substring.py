"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                c += 1
                r += 1
                l -= 1

            l, r = i, i +1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                c += 1
                r += 1
                l -= 1
        return c


if __name__ == '__main__':
    s = "babad"
    s = "aaa"
    # s = "ba"
    # nums = [1,2,1,1]
    # nums = [1,2,3,1]
    res = Solution().countSubstrings(s)
    print(res)
