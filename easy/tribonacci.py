"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""


class Solution:
    memo = {}
    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n < 2:
            return n
        if n == 2:
            return 1
        res = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.memo[n] = res
        return res
