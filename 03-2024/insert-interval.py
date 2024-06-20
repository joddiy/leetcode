import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        while i < len(intervals):
            if intervals[i][0] >= newInterval[0]:
                break
            else:
                i += 1
        intervals.insert(i, newInterval)
        ret = []
        for inter in intervals:
            if len(ret) > 0 and inter[0] <= ret[-1][1]:
                ret[-1][1] = max(inter[1], ret[-1][1])
            else:
                ret.append(inter)
        return ret


solution = Solution().insert
solution(intervals=[[1, 3], [6, 9]], newInterval=[2, 5])
solution(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8])
