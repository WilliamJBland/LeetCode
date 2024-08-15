"""
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        def dp(char, depth):
            if depth == n:
                return 1
            return sum(dp(vowel, depth + 1) for vowel in ['a', 'e', 'i', 'o', 'u'] if char <= vowel)
        return dp('a', 0)

if __name__ == '__main__':
    res = Solution().countVowelStrings(2)
    print(res)

