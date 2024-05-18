import sys

from tools import *
import pprint


class Solution(object):
    # @print_
    # def romanToInt(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     value_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     stack = []
    #     ret = 0
    #     for c in s:
    #         if c in ('V', 'X') and len(stack) and stack[-1] == 'I':
    #             ret += value_map[c] - value_map[stack.pop(-1)]
    #         elif c in ('L', 'C') and len(stack) and stack[-1] == 'X':
    #             ret += value_map[c] - value_map[stack.pop(-1)]
    #         elif c in ('D', 'M') and len(stack) and stack[-1] == 'C':
    #             ret += value_map[c] - value_map[stack.pop(-1)]
    #         elif c in ('I', 'X', 'C'):
    #             stack.append(c)
    #         else:
    #             ret += value_map[c]
    #     while stack:
    #         ret += value_map[stack.pop(-1)]
    #     return ret

    @print_
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ret = 0
        stack = []
        for c in s:
            i = value_map[c]
            while stack and i > stack[-1]:
                ret -= stack.pop(-1)
            stack.append(i)
        return sum(stack) + ret


solution = Solution().romanToInt
solution(s="III")
solution(s="IV")
solution(s="LVIII")
solution(s="MCMXCIV")
