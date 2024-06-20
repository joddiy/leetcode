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
        map_ = defaultdict(set)
        for x, y in prerequisites:
            map_[x].add(y)

        visited = [0] * numCourses  # 0, -1, 1

        ret = []

        def check(c):
            if visited[c] == -1:
                return False
            elif visited[c] == 1:
                return True
            else:
                visited[c] = -1
                for n in map_[c]:
                    if not check(n):
                        return False
                visited[c] = 1
                ret.append(c)
                return True

        for i in range(numCourses):
            if not check(i):
                return []

        for i in range(numCourses):
            if i not in ret:
                ret.append(i)

        return ret


solution = Solution().findOrder
solution(numCourses=2, prerequisites=[[1, 0]])
solution(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]])
solution(numCourses=1, prerequisites=[])
