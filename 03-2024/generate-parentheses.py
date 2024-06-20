import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []

        def recursive(prefix, l, r):  # exist_l, allow_r
            if len(prefix) == 2 * n:
                ret.append(prefix)
            else:
                if l < n:
                    recursive(prefix + "(", l + 1, r + 1)
                if r > 0:
                    recursive(prefix + ")", l, r - 1)

        recursive("", 0, 0)
        return ret


solution = Solution().generateParenthesis
solution(n=3)
