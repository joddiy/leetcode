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
        map_ = defaultdict(dict)
        stack = []
        for (a, b), v in zip(equations, values):
            stack.append((a, b, v))
            stack.append((b, a, 1. / v))
        while stack:
            a, b, v = stack.pop(0)
            if b in map_[a]:
                continue
            map_[a][a] = 1.
            map_[b][b] = 1.
            map_[a][b] = v
            map_[b][a] = 1. / v
            # a, b, c -> a/b * b/c
            for c, v2 in map_[b].items():
                stack.append((a, c, v * v2))
            # b, a, c -> b/a * a/c
            for c, v2 in map_[a].items():
                stack.append((b, c, 1./ v * v2))

        ret = []
        for a, b in queries:
            if a in map_ and b in map_[a]:
                ret.append(map_[a][b])
            else:
                ret.append(-1.)
        return ret


solution = Solution().calcEquation
solution(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
         queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
# solution(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
#          queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]])
# solution(equations=[["a", "b"]], values=[0.5], queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]])
