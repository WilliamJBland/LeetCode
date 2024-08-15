"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_vol = 0
        while l < r:
            max_vol = max(max_vol, (r-l) * min(height[r], height[l]))
            if height[r] <= height[l]:
                r -= 1
            else:
                l +=1
        return max_vol



if __name__ == '__main__':
    res = Solution().maxArea([1,8,6,2,5,4,8,3,7])
    print(res)