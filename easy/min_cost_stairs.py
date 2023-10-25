"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you
can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

[2, 5, 10, 1, 1]
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(3, len(cost) + 1):
            j = len(cost) - i
            cost[j] += min(cost[j+1], cost[j+2])
        return min(cost[0], cost[1])


if __name__ == '__main__':
    cost_1 = [10,15,20]
    cost_2 = [1,100,1,1,1,100,1,1,100,1]
    res = Solution().minCostClimbingStairs(cost=cost_2)
    print(res)
