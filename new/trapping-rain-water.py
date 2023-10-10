import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height = [0] + height + [0]
        n = len(height)
        left_most = [0] * n
        right_most = [0] * n

        for i in range(1, n):
            left_most[i] = max(height[i], left_most[i - 1])

        for i in range(n - 2, -1, -1):
            right_most[i] = max(height[i], right_most[i + 1])

        area = 0
        for i in range(1, n - 1):
            area += max(min(left_most[i - 1], right_most[i + 1]) - height[i], 0)

        return area


solution = Solution().trap
solution(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
solution(height=[4, 2, 0, 3, 2, 5])
