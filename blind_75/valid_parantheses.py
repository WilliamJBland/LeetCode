"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(', '{', '[']
        closes = [')', '}', ']']
        stack = []
        for char in s:
            if char in opens:
                stack.append(char)
            else:
                if not stack or stack.pop() != opens[closes.index(char)]:
                    return False
        return True if stack == [] else False


if __name__ == '__main__':
    res = Solution().isValid("()[{(())}]{}")
    print(res)
