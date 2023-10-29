"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        max_freq = 1
        counts = {}
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_freq = max(max_freq, counts[s[r]])
            if (r-l+1) - max_freq <= k:
                res = max(r-l+1, res)
                r += 1
                if r == len(s):
                    return res
            else:
                counts[s[l]] -= 1
                l += 1
        return res





if __name__ == '__main__':
    res = Solution().characterReplacement("AABABBA", 1)
    print(res)
    # res = Solution().characterReplacement("A", 0)
    # print(res)