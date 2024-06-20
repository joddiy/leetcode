import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c not in ("+", "-", "*", "/"):
                stack.append(float(c))
            else:
                a, b = stack.pop(), stack.pop()
                if c == '+':
                    v = b + a
                elif c == '-':
                    v = b - a
                elif c == '*':
                    v = b * a
                else:
                    v = b / a
                    v = math.floor(v) if v > 0 else math.ceil(v)
                stack.append(v)

        return int(stack[0])


solution = Solution().evalRPN
# solution(tokens=["2", "1", "+", "3", "*"])
# solution(tokens=["4", "13", "5", "/", "+"])
solution(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
