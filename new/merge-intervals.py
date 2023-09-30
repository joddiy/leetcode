import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        ret = [intervals.pop(0)]
        while intervals:
            tmp = intervals.pop(0)
            if tmp[0] <= ret[-1][1]:
                ret[-1][1] = max(tmp[1], ret[-1][1])
            else:
                ret.append(tmp)
        return ret


solution = Solution().merge
solution(intervals=[[1, 4], [0, 4]])
solution(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
solution(intervals=[[1, 4], [4, 5]])
solution(intervals=[[1, 4], [2, 3]])
solution(intervals=[[1, 4]])
