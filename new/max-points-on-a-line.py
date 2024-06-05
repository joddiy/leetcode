import math
import pprint
import sys

from tools import *
from collections import Counter

import heapq


class Solution(object):
    @print_
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 1
        for i in range(len(points)):
            x, counts = points[i], Counter()
            for j in range(i + 1, len(points)):
                y = points[j]
                if x[0] == y[0]:  # denonminator is zero, vertical line
                    slope = float('inf')
                else:
                    slope = (y[1] - x[1]) * 1.0 / (y[0] - x[0])
                counts[slope] += 1
                res = max(res, counts[slope] + 1)
        return res


solution = Solution().maxPoints
solution(points=[[1, 1], [2, 2], [3, 3]])
solution(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
