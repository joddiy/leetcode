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
        for p in points:
            if ret and ret[-1][1] >= p[0]:
                ret[-1][0] = max(ret[-1][0], p[0])
                ret[-1][1] = min(ret[-1][1], p[1])
            else:
                ret.append(p)
        return len(ret)


solution = Solution().findMinArrowShots
solution(points=[[10, 16], [2, 8], [1, 6], [7, 12]])
solution(points=[[1, 2], [3, 4], [5, 6], [7, 8]])
solution(points=[[1, 2], [2, 3], [3, 4], [4, 5]])
