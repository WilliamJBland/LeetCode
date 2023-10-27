"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for w in strs:
            s_w = ''.join(sorted(w))
            if s_w in ans:
                ans[s_w].append(w)
            else:
                ans[s_w] = [w]
        return [l for l in ans.values()]

if __name__ == '__main__':
    res = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(res)