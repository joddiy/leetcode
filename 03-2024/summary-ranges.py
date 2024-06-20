import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ret = [[]]
        for n in nums:
            if len(ret[-1]) < 1:
                ret[-1].append(n)
            elif n == ret[-1][-1] + 1:
                ret[-1].append(n)
            else:
                ret.append([n])
        ret_new = []
        for x in ret:
            if len(x) >= 2:
                ret_new.append(str(x[0]) + "->" + str(x[-1]))
            else:
                ret_new.append(str(x[0]))
        return ret_new
        # return ["->".join([str(y) for y in x]) for x in ret]


solution = Solution().summaryRanges
solution(nums=[0, 1, 2, 4, 5, 7])
solution(nums=[0, 2, 3, 4, 6, 8, 9])
