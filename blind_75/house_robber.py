"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.


"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums[2] = max(nums[2] + nums[0], nums[1])
        for i in range(3, len(nums)):
            nums[i] = max(max(nums[i - 2], nums[i - 3]) + nums[i], nums[i - 1])
        return nums[-1]


if __name__ == '__main__':
    nums = [2,7,9,3,1]
    # nums = [1,2,3,1]
    res = Solution().rob(nums)
    print(res)
