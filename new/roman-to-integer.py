import pprint

from tools import *


class Solution(object):
    @print_
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        conv = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        stack = []
        minus = 0
        for i in range(len(s)):
            v = conv[s[i]]
            while stack and v > stack[-1]:
                minus += stack.pop()
            stack.append(v)
        return sum(stack) - minus

solution = Solution().romanToInt
solution("III")
solution("LVIII")
solution("MCMXCIV")
