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
        for t in tokens:
            if t == "+":
                a, b = stack.pop(-1), stack.pop(-1)
                stack.append(b + a)
            elif t == "-":
                a, b = stack.pop(-1), stack.pop(-1)
                stack.append(b - a)
            elif t == "*":
                a, b = stack.pop(-1), stack.pop(-1)
                stack.append(b * a)
            elif t == "/":
                a, b = stack.pop(-1), stack.pop(-1)
                t = b / a
                if t > 0:
                    t = math.floor(t)
                else:
                    t = math.ceil(t)
                stack.append(t)
            else:
                stack.append(float(t))
        return int(stack[-1])


solution = Solution().evalRPN
# solution(tokens=["2", "1", "+", "3", "*"])
# solution(tokens=["4", "13", "5", "/", "+"])
solution(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
