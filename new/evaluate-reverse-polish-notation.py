import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        while tokens:
            t = tokens.pop(0)
            if t == "+":
                v2, v1 = stack.pop(), stack.pop()
                stack.append(v1 + v2)
            elif t == "-":
                v2, v1 = stack.pop(), stack.pop()
                stack.append(v1 - v2)
            elif t == "*":
                v2, v1 = stack.pop(), stack.pop()
                stack.append(v1 * v2)
            elif t == "/":
                v2, v1 = stack.pop(), stack.pop()
                v_ = v1 / v2
                if v_ < 0:
                    v_ = math.ceil(v_)
                else:
                    v_ = math.floor(v_)
                stack.append(v_)
            else:
                stack.append(float(t))
        return int(stack[0])


solution = Solution().evalRPN
solution(tokens=["2", "1", "+", "3", "*"])
solution(tokens=["4", "13", "5", "/", "+"])
solution(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
