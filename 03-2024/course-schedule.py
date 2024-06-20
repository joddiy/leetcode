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
        map_ = defaultdict(set)
        for x, y in prerequisites:
            map_[x].add(y)

        visited = [0] * numCourses  # 0, -1, 1

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
                return True

        for i in range(numCourses):
            if not check(i):
                return False

        return True


solution = Solution().canFinish
solution(numCourses=2, prerequisites=[[1, 0]])
solution(numCourses=2, prerequisites=[[1, 0], [0, 1]])
solution(numCourses=5, prerequisites=[[1, 4], [2, 4], [3, 1], [3, 2]])
solution(numCourses=3, prerequisites=[[0, 1], [0, 2], [1, 2]])
