from tools import *


class Solution(object):
    @print_
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # search first invalid num from the end
        cur_min = nums[-1]
        ret_l = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] > cur_min:
                ret_l = i
            cur_min = min(cur_min, nums[i])

        # search last invalid num from the start
        cur_max = nums[0]
        ret_r = 0
        for i in range(n):
            if nums[i] < cur_max:
                ret_r = i
            cur_max = max(cur_max, nums[i])

        return ret_r - ret_l + 1 if ret_r > ret_l else 0


solution = Solution().findUnsortedSubarray

solution([2, 6, 4, 8, 10, 9, 15])
solution([1, 2, 3, 4, 5])
solution([1])
solution([1, 3, 2, 2, 2])