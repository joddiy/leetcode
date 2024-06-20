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
        array = [[nums1[0] + nums2[0], 0, 0]]
        ret = []
        heapq.heapify(ret)
        while array and len(ret) < k:
            sum_, i, j = heapq.heappop(array)
            ret.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1):
                heapq.heappush(array, (nums1[i + 1] + nums2[j], i + 1, j))
            if j + 1 < len(nums2):
                heapq.heappush(array, (nums1[i] + nums2[j + 1], i, j + 1))
        return ret


solution = Solution().kSmallestPairs
solution(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3)
solution(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2)
