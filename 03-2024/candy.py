import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        ret = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        for i in range(n):
            ret[i] = max(left[i], right[i])

        return sum(ret)


solution = Solution().candy
solution(ratings=[1, 0, 2])
solution(ratings=[1, 2, 2])
