from tools import *


class Solution(object):
    @print_
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        ret = [intervals.pop(0)]
        for tmp in intervals:
            if tmp[0] <= ret[-1][1]:
                if tmp[1] <= ret[-1][1]:
                    continue
                else:
                    ret[-1][1] = tmp[1]
            else:
                ret.append(tmp)
        return ret

solution = Solution().merge
solution([[2, 6], [1, 3], [8, 10], [15, 18]])
solution([[1, 4], [2, 3]])