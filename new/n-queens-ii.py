import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def solve(columns, diffs, sums):
            row = len(columns)
            if row == n:
                return 1
            res = 0
            for column in range(n):
                if column not in columns and row - column not in diffs and row + column not in sums:
                    columns.add(column)
                    diffs.add(row - column)
                    sums.add(row + column)
                    res += solve(columns, diffs, sums)
                    columns.remove(column)
                    diffs.remove(row - column)
                    sums.remove(row + column)
            return res
        return solve(set(), set(), set())

solution = Solution().totalNQueens
solution(n=4)
solution(n=1)
