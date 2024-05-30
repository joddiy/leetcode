import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        grid = defaultdict(set)
        for x, y in prerequisites:
            grid[x].add(y)

        visited = [0] * numCourses  # 0: not visited, -1: visited, 1: not cycle

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
                return True

        for i in range(numCourses):
            if not recursive(i):
                return False
        return True

solution = Solution().canFinish
solution(numCourses=2, prerequisites=[[1, 0]])
solution(numCourses=2, prerequisites=[[1, 0], [0, 1]])
solution(numCourses=5, prerequisites=[[1, 4], [2, 4], [3, 1], [3, 2]])
solution(numCourses=3, prerequisites=[[0, 1], [0, 2], [1, 2]])
