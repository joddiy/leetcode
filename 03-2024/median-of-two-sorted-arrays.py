import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        h = (m + n + 1) // 2

        def find(s, e):
            i = (s + e) // 2
            j = h - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                # notice: new idx is (s, i-1)
                return find(s, i - 1)
            elif i < m and nums2[j - 1] > nums1[i]:
                # notice: new idx is (i+1, e)
                return find(i + 1, e)
            else:
                l, r = 0, 0
                if i == 0:
                    l = nums2[j - 1]
                elif j == 0:
                    l = nums1[i - 1]
                else:
                    l = max(nums1[i - 1], nums2[j - 1])

                # if the lenght is odd
                if (m + n) % 2 == 1:
                    return l

                # else the length is even
                if i == m:
                    r = nums2[j]
                elif j == n:
                    r = nums1[i]
                else:
                    r = min(nums1[i], nums2[j])
                return (l + r) / 2.

        return find(0, m)


solution = Solution().findMedianSortedArrays
solution(nums1=[1, 3], nums2=[2])
solution(nums1=[1, 2], nums2=[3, 4])
