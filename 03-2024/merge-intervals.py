import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        ret = []
        for inter in intervals:
            if len(ret) > 0 and inter[0] <= ret[-1][1]:
                ret[-1][1] = max(inter[1], ret[-1][1])
            else:
                ret.append(inter)
        return ret


solution = Solution().merge
solution(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
solution(intervals=[[1, 4], [4, 5]])
solution(intervals=[[1, 4]])
