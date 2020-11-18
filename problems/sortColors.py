from tools import *


class Solution(object):
    @print_
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # i indicates the first position to be replace be 0
        # k indicates the first position to be replace be 2
        i, j, k = 0, 0, n - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j = max(j, i)
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            else:
                j += 1
        return nums


solution = Solution().sortColors

solution([2, 0, 2, 1, 1, 0])
solution([1, 2, 0])
