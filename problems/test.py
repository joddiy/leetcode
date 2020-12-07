from tools import *
import sys
from collections import defaultdict
from collections import Counter
import heapq
import math


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        ret = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ == 0:
                    ret.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum_ < 0:
                    j += 1
                else:
                    k -= 1

        return ret


solution = Solution().threeSum

print(solution([-1, 0, 1, 2, -1, -4]))
