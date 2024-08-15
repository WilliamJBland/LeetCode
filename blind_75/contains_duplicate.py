"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if
every element is distinct.

"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        check = set()
        for n in nums:
            if n in check:
                return True
            check.add(n)
        return False