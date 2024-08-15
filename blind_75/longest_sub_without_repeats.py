"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            if not s:
                return 0
            l = 0
            longest_sub = 1
            seen = {s[0]: 0}
            for r in range(1, len(s)):
                if s[r] not in seen or seen[s[r]] < l:
                    longest_sub = max(longest_sub, r-l + 1)
                else:
                    l = seen[s[r]] + 1
                seen[s[r]] = r
            return longest_sub




if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring("tmmzuxt")
    # res = Solution().lengthOfLongestSubstring("p")
    # res = Solution().lengthOfLongestSubstring("")
    print(res)