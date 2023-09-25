import pprint

from tools import *


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        tmp = [0] * len(nums1)
        i, j, k = 0, 0, 0
        while i < m or j < n:
            if i == m:
                tmp[k] = nums2[j]
                j += 1
            elif j == n:
                tmp[k] = nums1[i]
                i += 1
            elif nums1[i] <= nums2[j]:
                tmp[k] = nums1[i]
                i += 1
            else:
                tmp[k] = nums2[j]
                j += 1
            k += 1
        for i in range(len(nums1)):
            nums1[i] = tmp[i]


solution = Solution().merge

solution([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
solution([1], 1, [], 0)
solution([0], 0, [1], 1)
solution([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
