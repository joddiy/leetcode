import sys

from tools import *
import pprint


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        j = n - k
        # (nums[:-k][::-1] + nums[-k:][::-1])[::-1]
        for i in range(j // 2):
            nums[i], nums[j - 1 - i] = nums[j - 1 - i], nums[i]
        for i in range(k // 2):
            nums[j + i], nums[j + k - 1 - i] = nums[j + k - 1 - i], nums[j + i]
        for i in range(n // 2):
            nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]


solution = Solution().rotate
solution(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
solution(nums=[-1, -100, 3, 99], k=2)
