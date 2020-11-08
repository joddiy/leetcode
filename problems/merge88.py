from tools import *


class Solution(object):
    @print_
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while j < n:
            if i >= m:
                j += 1
            elif nums1[i] > nums2[j]:
                
            i += 1
        return nums1


solution = Solution().merge

# solution([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
solution([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)