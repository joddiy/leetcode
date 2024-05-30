import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        grid = defaultdict(set)
        for x, y in prerequisites:
            grid[x].add(y)

        visited = [0] * numCourses  # 0: not visited, -1: visited, 1: not cycle

        ret = []

        def recursive(c):
            if visited[c] == 1 or c not in grid:
                return True
            elif visited[c] == -1:
                return False
            else:
                visited[c] = -1
                for c_ in grid[c]:
                    if not recursive(c_):
                        return False
                visited[c] = 1
                ret.append(c)
                return True

        for i in range(numCourses):
            if not recursive(i):
                return []

        for i in range(numCourses):
            if i not in grid:
                ret.insert(0, i)
        return ret


solution = Solution().findOrder
solution(numCourses=2, prerequisites=[[1, 0]])
solution(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]])
