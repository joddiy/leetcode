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
        n = len(height)
        left = [0] * n
        right = [0] * n
        cur_max = 0
        for i in range(n):
            left[i] = cur_max
            cur_max = max(cur_max, height[i])
        cur_max = 0
        for i in range(n - 1, -1, -1):
            right[i] = cur_max
            cur_max = max(cur_max, height[i])
        ret = 0
        for i in range(n):
            ret += max(min(left[i], right[i]) - height[i], 0)

        return ret


solution = Solution().trap
solution(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
solution(height=[4, 2, 0, 3, 2, 5])
