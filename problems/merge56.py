from tools import *

class Solution(object):
    @print_
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda  x: x[0])
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            int_ = intervals[i]
            if int_[0] <= ret[-1][1]:
                ret[-1][1] = max(int_[1], ret[-1][1])
            else:
                ret.append(int_)
        return ret
        

solution = Solution().merge
solution([[2, 6], [1, 3], [8, 10], [15, 18]])
solution([[1, 4], [2, 3]])