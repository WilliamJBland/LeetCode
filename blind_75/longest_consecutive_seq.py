"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        lookup = set(nums)
        max_seq_size = 0
        for i in lookup:
            if i - 1 not in lookup:
                j = 1
                while i + j in lookup:
                    j += 1
                max_seq_size = max(max_seq_size, j)
        return max_seq_size


if __name__ == '__main__':
    res = Solution().longestConsecutive([2, 5, 10, 3, 4, 11, 6])

    print(res)