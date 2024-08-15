"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence
 of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation."""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        i = len(s) - 1
        dp[len(s)] = True
        while i >= 0:
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break
            i -= 1
        return dp[0]

if __name__ == "__main__":
    d = {"leet", "code"}
    r = Solution().wordBreak("leetcodes", d)
    print(r)