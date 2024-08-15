"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        store = {}
        for i in nums:
            store[i] = store[i] + 1 if i in store else 1
        return sorted(store, key=lambda k: -store[k])[:k]

if __name__ == '__main__':
    n = [1,2,2,3,9,9]
    res = Solution().topKFrequent(n, 2)
    print(res)