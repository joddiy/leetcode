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
        # i indicates the last value of num1
        # j indicates the last value of num2
        # k indicates the last zero
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i < 0 or nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k], nums1[i] = nums1[i], nums1[k]
                i -= 1
            k -= 1
        pprint.pprint(nums1)


solution = Solution().merge

solution([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
solution([1], 1, [], 0)
solution([0], 0, [1], 1)
solution([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
