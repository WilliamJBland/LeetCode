"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_length = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > res_length:
                    res_length = r - l + 1
                    res = s[l:r+1]
                r += 1
                l -= 1

            l, r = i, i +1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > res_length:
                    res_length = r - l + 1
                    res = s[l:r + 1]
                r += 1
                l -= 1
        return res



if __name__ == '__main__':
    s = "babad"
    s = "baaba"
    s = "ba"
    # nums = [1,2,1,1]
    # nums = [1,2,3,1]
    res = Solution().longestPalindrome(s)
    print(res)
