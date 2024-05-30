import math
import pprint
import sys

from tools import *
from collections import defaultdict
import heapq


class Solution(object):
    @print_
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = []
        heapq.heapify(ret)
        i = 0
        while i < k:
            heapq.heappush(ret, nums[i])
            i += 1
        while i < len(nums):
            heapq.heappush(ret, nums[i])
            heapq.heappop(ret)
            i += 1
        return heapq.heappop(ret)


solution = Solution().findKthLargest
solution(nums=[3, 2, 1, 5, 6, 4], k=2)
solution(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)
