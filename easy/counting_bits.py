"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

0: 0 0 0 0 -> 0
1: 0 0 0 1 -> 1 + dp(0) -> 1 + dp(n-1)
2: 0 0 1 0 -> 1 + dp(0) -> 1 + dp(n-2)
3: 0 0 1 1 -> 1 + dp(1) -> 1 + dp(n-2)
4: 0 1 0 0 -> 1 + dp(0) -> 1 + dp(n-4)
5: 0 1 0 1 -> 1 + dp(1) -> 1 + dp(n-4)
6: 0 1 1 0 -> 1 + dp(2) -> 1 + dp(n-4)
7: 0 1 1 1 -> 1 + dp(3) -> 1 + dp(n-4)
8: 1 0 0 0 -> 1 + dp(0) -> 1 + dp(n-8)

"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0 for _ in range(n + 1)]
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            res[i] = 1 + res[i - offset]
        return res




if __name__ == '__main__':
    res = Solution().countBits(n=2)
    print(res)
