import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []

        # lu, means how many "(" has been used, if left == n, then can only give ")"
        # lr, means how many single "(" has been remained, for example "(()", the two "(" only has one singe remained
        def recursive(cur_ret, lu, lr):
            if len(cur_ret) < n * 2:
                if lu < n:
                    recursive(cur_ret + "(", lu + 1, lr + 1)
                if lr > 0:
                    recursive(cur_ret + ")", lu, lr - 1)
            else:
                ret.append(cur_ret)

        recursive("", 0, 0)
        return ret


solution = Solution().generateParenthesis
solution(n=3)
