import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        for i in range(len(nums)):
            if i == 0:
                ret.append([nums[i]])
            elif i == len(nums) - 1 and nums[i] == nums[i - 1] + 1:
                ret[-1].append(nums[i])
            elif nums[i] != nums[i - 1] + 1:
                ret[-1].append(nums[i - 1])
                ret.append([nums[i]])

        for i in range(len(ret)):
            if len(ret[i]) == 1 or ret[i][0] == ret[i][1]:
                ret[i] = str(ret[i][0])
            else:
                ret[i] = str(ret[i][0]) + "->" + str(ret[i][1])

        return ret


solution = Solution().summaryRanges
solution(nums=[0, 1, 2, 4, 5, 7])
solution(nums=[0, 2, 3, 4, 6, 8, 9])
