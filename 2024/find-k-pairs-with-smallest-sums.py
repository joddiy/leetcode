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
        m, n = len(nums1), len(nums2)
        visited = set()
        ret = []
        while k and heap_:
            v, i, j = heapq.heappop(heap_)
            ret.append([nums1[i], nums2[j]])
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(heap_, [nums1[i + 1] + nums2[j], i + 1, j])
                visited.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(heap_, [nums1[i] + nums2[j + 1], i, j + 1])
                visited.add((i, j + 1))
            k -= 1
        return ret


solution = Solution().kSmallestPairs
solution(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3)
solution(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2)
