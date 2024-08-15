"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
 rob tonight without alerting the police.

"""
from typing import List


class Solution:
    def _rob(self, nums):
        if len(nums) <= 2:
            return max(nums)

        nums[2] = max(nums[2] + nums[0], nums[1])
        for i in range(3, len(nums)):
            nums[i] = max(max(nums[i - 2], nums[i - 3]) + nums[i], nums[i - 1])
        return nums[-1]
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[:-1]), self. _rob(nums[1:]))

if __name__ == '__main__':
    nums = [200,3,140,20,10]
    # nums = [1,2,1,1]
    # nums = [1,2,3,1]
    res = Solution().rob(nums)
    print(res)
