import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums1 = nums[:(n - k)][::-1]
        nums2 = nums[(n - k):][::-1]
        for i, n_ in enumerate((nums1 + nums2)[::-1]):
            nums[i] = n_
        return nums


solution = Solution().rotate
solution(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
# solution(nums=[-1, -100, 3, 99], k=2)
