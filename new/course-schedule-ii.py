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
        path = defaultdict(set)
        for p1, p2 in prerequisites:
            path[p1].add(p2)

        visited = [0] * numCourses  # 0: not visited, -1: visited, 1: not cycle

        ret = []

        def recursive(c):
            if visited[c] == 1 or c not in path:
                return True
            elif visited[c] == -1:
                return False
            else:
                visited[c] = -1
                for c_ in path[c]:
                    if not recursive(c_):
                        return False
                ret.append(c)
                visited[c] = 1
                return True

        for course in list(path.keys()):
            if not recursive(course):
                return []

        for i in range(numCourses):
            if i not in path:
                ret.insert(0, i)
        return ret


solution = Solution().findOrder
solution(numCourses=2, prerequisites=[[1, 0]])
solution(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]])
