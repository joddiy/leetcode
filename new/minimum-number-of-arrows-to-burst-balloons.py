import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: x[0])
        ret = 0

        interval = None
        while points:
            point_ = points.pop(0)
            if interval is None:
                interval = point_
            elif point_[0] <= interval[1]:
                interval[0] = max(interval[0], point_[0])
                interval[1] = min(interval[1], point_[1])
            else:
                ret += 1
                interval = point_
        if interval:
            ret += 1
        return ret


solution = Solution().findMinArrowShots
solution(points=[[10, 16], [2, 8], [1, 6], [7, 12]])
solution(points=[[1, 2], [3, 4], [5, 6], [7, 8]])
solution(points=[[1, 2], [2, 3], [3, 4], [4, 5]])
