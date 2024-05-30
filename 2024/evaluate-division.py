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
        grid = defaultdict(dict)
        array = []
        for (x, y), v in zip(equations, values):
            array.append((x, y, v))
        while array:
            x, y, v = array.pop(0)
            if y in grid[x]:
                continue
            grid[x][x] = 1.
            grid[y][y] = 1.
            grid[x][y] = v
            grid[y][x] = 1. / v
            for z, v_ in grid[y].items():
                array.append((x, z, v * v_))
            for z, v_ in grid[x].items():
                array.append((y, z, 1. / v * v_))
        ret = []
        for x, y in queries:
            if x in grid and y in grid[x]:
                ret.append(grid[x][y])
            else:
                ret.append(-1.)

        return ret


solution = Solution().calcEquation
solution(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
         queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
solution(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
         queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]])
solution(equations=[["a", "b"]], values=[0.5], queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]])
