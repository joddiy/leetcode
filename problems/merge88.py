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
        i, j = m - 1, n - 1
        k = len(nums1) - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[i], nums1[k] = nums1[k], nums1[i]
                i -= 1
            else:
                nums2[j], nums1[k] = nums1[k], nums2[j]
                j -= 1
            k -= 1

        while i >= 0:
            nums1[i], nums1[k] = nums1[k], nums1[i]
            k -= 1
            i -= 1

        while j >= 0:
            nums2[j], nums1[k] = nums1[k], nums2[j]
            k -= 1
            j -= 1
        return nums1


solution = Solution().merge

solution([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
solution([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)