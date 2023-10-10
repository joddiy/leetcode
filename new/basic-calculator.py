import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        number = 0
        sign = 1

        for c in s:
            if c.isdigit():
                number = 10 * number + int(c)
            elif c == '+':
                result += sign * number
                number = 0
                sign = 1
            elif c == '-':
                result += sign * number
                number = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ')':
                result += sign * number
                number = 0
                result *= stack.pop()  # Pop the sign before the parenthesis
                result += stack.pop()  # Pop the result calculated before the parenthesis

        if number != 0:
            result += sign * number

        return result


solution = Solution().calculate
solution(s="1 + 1")
solution(s=" 2-1 + 2 ")
solution(s="(1+(4+5+2)-3)+(6+8)")
solution(s="(1)")
solution(s="2147483647")
solution(s="1-(     -2)")
solution(s="- (3 + (4 + 5))")
