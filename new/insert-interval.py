import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # insert
        i = 0
        while i < len(intervals):
            if newInterval[0] >= intervals[i][0]:
                i += 1
            else:
                break
        intervals.insert(i, newInterval)
        # merge
        ret = [intervals.pop(0)]
        while intervals:
            tmp = intervals.pop(0)
            if tmp[0] <= ret[-1][1]:
                ret[-1][1] = max(tmp[1], ret[-1][1])
            else:
                ret.append(tmp)
        return ret



solution = Solution().insert
solution(intervals=[[1, 3], [6, 9]], newInterval=[2, 5])
solution(intervals=[[1, 3], [6, 9]], newInterval=[7, 5])
solution(intervals=[[1, 3], [6, 9]], newInterval=[0, 5])
