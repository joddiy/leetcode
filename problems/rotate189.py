from tools import *


class Solution(object):
    @print_
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k:
            nums.insert(0, nums.pop(-1))
            k -= 1
        return nums


solution = Solution().rotate

solution([1, 2, 3, 4, 5, 6, 7], 3)
