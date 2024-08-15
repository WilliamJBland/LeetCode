"""
You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums.
"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [0] * (n + 1)
        max_num = 0
        for i in range(n):
            if i <= 1:
                nums[i] = i
                max_num = max(max_num, i)
            if i >= 1:
                if 2 * i <= n:
                    nums[2 * i] = nums[i]
                    max_num = max(max_num, nums[2 * i])
                if (2 * i + 1) <= n:
                    nums[2 * i + 1] = nums[i] + nums[i + 1]
                    max_num = max(max_num, nums[2 * i + 1])
        return max_num



if __name__ == '__main__':
    res = Solution().getMaximumGenerated(1)
    print(res)

