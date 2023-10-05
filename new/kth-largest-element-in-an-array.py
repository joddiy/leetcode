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

        # solution 1
        # (n+k)logn
        # ret = []
        # heapq.heapify(ret)
        # for n in nums:
        #     heapq.heappush(ret, -n)
        # for i in range(k - 1):
        #     heapq.heappop(ret)
        # return -heapq.heappop(ret)

        # solution 2
        # nlogk
        # ret = nums[:k]
        # heapq.heapify(ret)
        # for n in nums[k:]:
        #     heapq.heappushpop(ret, n)
        # return heapq.heappop(ret)

        # solution 3
        def find(cur_nums, cur_k):
            m = (len(cur_nums) - 1) // 2
            larger = [n for n in cur_nums if n > cur_nums[m]]
            lal = len(larger)
            lql = sum([1 for n in cur_nums if n == cur_nums[m]])
            if lal < cur_k <= lal + lql:
                return cur_nums[m]
            elif cur_k <= lal:
                return find(larger, cur_k)
            else:
                less = [n for n in cur_nums if n < cur_nums[m]]
                return find(less, cur_k - lal - lql)

        return find(nums, k)


solution = Solution().findKthLargest
solution(nums=[3, 2, 1, 5, 6, 4], k=2)
solution(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)
solution(nums=[-1, 2, 0], k=2)
