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

        def recursive(prefix, lu, lr):
            if len(prefix) == 2 * n:
                ret.append(prefix)
                return
            if lu < n:
                recursive(prefix + "(", lu + 1, lr + 1)
            if lr > 0:
                recursive(prefix + ")", lu, lr - 1)

        recursive("", 0, 0)
        return ret


solution = Solution().generateParenthesis
solution(n=3)
