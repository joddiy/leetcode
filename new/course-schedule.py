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
        path = defaultdict(set)
        for p1, p2 in prerequisites:
            path[p2].add(p1)

        visited = [0] * numCourses  # 0: not visited, -1: visited, 1: not cycle

        def recursive(c):
            if visited[c] == 1:
                return True
            elif visited[c] == -1:
                return False
            else:
                visited[c] = -1
                for c_ in path[c]:
                    if not recursive(c_):
                        return False
                visited[c] = 1
                return True

        for course in list(path.keys()):
            if not recursive(course):
                return False
        return True


solution = Solution().canFinish
solution(numCourses=2, prerequisites=[[1, 0]])
solution(numCourses=2, prerequisites=[[1, 0], [0, 1]])
