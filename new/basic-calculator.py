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
        sign = 1
        number = 0

        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            else:
                if c == '+':
                    result += sign * number
                    sign = 1
                elif c == '-':
                    result += sign * number
                    sign = -1
                elif c == '(':
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                elif c == ')':
                    result += sign * number
                    result *= stack.pop()
                    result += stack.pop()
                else:
                    continue
                number = 0
        if number > 0:
            result += sign * number
        return result


solution = Solution().calculate
# solution(s="1 + 1")
# solution(s=" 2-1 + 2 ")
# solution(s="(1+(4+5+2)-3)+(6+8)")
# solution(s="(1)")
# solution(s="2147483647")
solution(s="1-(     -2)")
# solution(s="- (3 + (4 + 5))")
