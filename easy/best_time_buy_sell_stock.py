"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

1  10 4 3 1 100

10 1  2 1 3 2

2  4  1  6

buy low sell high
buy must come before sell
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if (s := len(prices)) < 2:
            return 0
        l, r = 0, 1
        max_profit = max(0, prices[r] - prices[l])
        for r in range(1, s - 1):
            if prices[l] > prices[r]:
                l = r
            max_profit = max(max_profit, prices[r + 1] - prices[l])
        return max(0, max_profit)





if __name__ == '__main__':
    res = Solution().maxProfit([7,1,5,3,6,4])
    # res = Solution().maxProfit([2, 4, 1])
    # res = Solution().maxProfit([1, 2])
    res = Solution().maxProfit([2,1,2,1,0,1,2])
    res = Solution().maxProfit([1,2,4])
    print(res)

