"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring,
 return the empty string "".

The testcases will be generated such that the answer is unique.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        t_dict = {}
        window_dict = {}
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1 # + t_dict.get(i, 0)
        current_min = len(s)
        min_word = ""
        window_dict[s[r]] = 1 + window_dict.get(s[r], 0)
        for r in range(len(s)):
            if all(window_dict.get(k, 0) >= t_dict[k] for k in t_dict):
                if r - l + 1 <= current_min:
                    current_min = r -l +1
                    min_word = s[l:r +1]
                l += 1
                if s[l-1] in window_dict:
                    window_dict[s[l-1]] -= 1
            else:
                if r < len(s):
                    if s[r] in t_dict:
                        window_dict[s[r]] = 1 + window_dict.get(s[r], 0)
                else:
                    l += 1
                    if s[l - 1] in window_dict:
                        window_dict[s[l - 1]] -= 1
        return min_word




if __name__ == '__main__':
    s = "a"
    t = "a"
    res = Solution().minWindow(s, t)
    print(res)