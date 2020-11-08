from tools import *


class Solution(object):
    @print_
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, k, j = 0, 0, len(nums) - 1
        while k <= j:
            if nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            elif nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            else:
                k += 1
        return nums


solution = Solution().sortColors

solution([2, 0, 2, 1, 1, 0])
solution([1, 2, 0])
