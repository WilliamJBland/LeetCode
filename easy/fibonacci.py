"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
the sum of the two preceding ones, starting from 0 and 1. Calculate F(n).
"""

class Solution:
    mem = {}
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        if n in self.mem:
            return self.mem[n]
        res = self.fib(n-1) + self.fib(n-2)
        self.mem[n] = res
        return res

if __name__ == '__main__':
    res = Solution().fib(n=100)
    print(res)
