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
        ret = 1
        for i in range(len(points)):
            x, cnt = points[i], Counter()
            for j in range(i + 1, len(points)):
                y = points[j]
                if x[0] == y[0]:
                    slope = float('inf')
                else:
                    slope = (y[1] - x[1]) * 1.0 / (y[0] - x[0])
                cnt[slope] += 1
                ret = max(ret, cnt[slope] + 1)
        return ret


solution = Solution().maxPoints
solution(points=[[1, 1], [2, 2], [3, 3]])
solution(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
