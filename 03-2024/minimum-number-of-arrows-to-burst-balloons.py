import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points)
        ret = []
        for i in range(len(points)):
            if not ret:
                ret.append(points[i])
            elif points[i][0] <= ret[-1][1]:
                ret[-1][0] = max(ret[-1][0], points[i][0])
                ret[-1][1] = min(ret[-1][1], points[i][1])
            else:
                ret.append(points[i])
        return len(ret)


solution = Solution().findMinArrowShots
solution(points=[[10, 16], [2, 8], [1, 6], [7, 12]])
solution(points=[[1, 2], [3, 4], [5, 6], [7, 8]])
solution(points=[[1, 2], [2, 3], [3, 4], [4, 5]])
