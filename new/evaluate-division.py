import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        table = defaultdict(dict)
        for equ, val in zip(equations, values):
            table[equ[0]][equ[1]] = val
            table[equ[1]][equ[0]] = 1. / val
            table[equ[1]][equ[1]] = 1.
            table[equ[0]][equ[0]] = 1.

        for k in table:
            for i in table[k]:
                for j in table[k]:
                    table[i][j] = table[i][k] * table[k][j]

        return [table[q1].get(q2, -1.0) for q1, q2 in queries]


solution = Solution().calcEquation
solution(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
         queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
