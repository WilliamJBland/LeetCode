"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i_counter = {}
        j_counter = {}
        for i, j in zip(s, t):
            new_i = i_counter[i] + 1 if i in i_counter else 1
            new_j = j_counter[j] + 1 if j in j_counter else 1
            i_counter[i] = new_i
            j_counter[j] = new_j
        return j_counter == i_counter

if __name__ == '__main__':
    res = Solution().isAnagram('hello', 'olleh')
    print(res)