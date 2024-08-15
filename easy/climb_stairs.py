"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Notice the fibonacci sequence
"""


class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        if n in self.memo:
            return self.memo[n]
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = res
        return res

if __name__ == '__main__':
    res = Solution().climbStairs(30)
    print(res)

