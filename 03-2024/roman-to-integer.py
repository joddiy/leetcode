import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        stack = []
        ret = 0
        for c in s:
            if stack and value_map[stack[-1]] < value_map[c]:
                ret -= value_map[stack.pop(-1)]
            stack.append(c)
        while stack:
            ret += value_map[stack.pop()]
        return ret


solution = Solution().romanToInt
solution(s="III")
solution(s="IV")
solution(s="LVIII")
solution(s="MCMXCIV")
