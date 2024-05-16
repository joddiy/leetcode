import sys

from tools import *
import pprint


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m or j < n:
            l, r = sys.maxsize, sys.maxsize
            if i < m:
                l = nums1[0]
            if j < n:
                r = nums2[0]
            if l < r:
                nums1.append(nums1.pop(0))
                i += 1
            else:
                nums1.append(nums2.pop(0))
                j += 1
        j = 0
        while j < n:
            nums1.pop(0)
            j += 1
        print(nums1)


solution = Solution().merge
solution(nums1=[4, 5, 6, 0, 0, 0], m=3, nums2=[1, 2, 3], n=3)
solution(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
solution(nums1=[1], m=1, nums2=[], n=0)
solution(nums1=[0], m=0, nums2=[1], n=1)
