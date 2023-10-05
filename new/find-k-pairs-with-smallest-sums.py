import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap_ = [[nums1[0] + nums2[0], 0, 0]]
        heapq.heapify(heap_)
        m, n = len(nums1), len(nums2)
        visited = set()
        ret = []
        while k and heap_:
            val, l_i, l_j = heapq.heappop(heap_)
            ret.append([nums1[l_i], nums2[l_j]])
            if l_i + 1 < m and (l_i+1, l_j) not in visited:
                heapq.heappush(heap_, [nums1[l_i + 1] + nums2[l_j], l_i + 1, l_j])
                visited.add((l_i + 1, l_j))
            if l_j + 1 < n and (l_i, l_j+1) not in visited:
                heapq.heappush(heap_, [nums1[l_i] + nums2[l_j + 1], l_i, l_j + 1])
                visited.add((l_i, l_j + 1))
            k = k - 1

        return ret


solution = Solution().kSmallestPairs
# solution(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3)
# solution(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2)
# solution(nums1=[1, 2], nums2=[3], k=3)
solution(nums1=[1, 1, 2], nums2=[1, 2, 3], k=10)
