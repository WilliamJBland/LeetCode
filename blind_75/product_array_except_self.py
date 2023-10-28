'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1] * len(nums)
        for i in range(len(nums) - 1):
            j = len(nums) - 1 - i
            prefix.append(nums[i] * prefix[i])
            postfix[j-1] = nums[j] * postfix[j]
        print(prefix)
        print(postfix)
        return [postfix[k] * prefix[k] for k in range(len(nums))]



if __name__ == '__main__':
    # res = Solution().productExceptSelf([1, 2, 3, 4])
    res = Solution().productExceptSelf([2,5,10, 3])

    print(res)