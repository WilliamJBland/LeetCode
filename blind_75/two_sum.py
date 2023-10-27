"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        check = {}
        for i in range(len(nums)):
            m = target - nums[i]
            if m in check:
                return [i, check[m]]
            check[nums[i]] = i



if __name__ == '__main__':
    res = Solution().twoSum([2,7,11,15], 9)
    # res = Solution().twoSum([3, 3], 6)
    # res = Solution().twoSum([2,2,3, 3, 2, 3], 6)
    print(res)