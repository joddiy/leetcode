import pprint

from tools import *


class Solution(object):
    @print_
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # solution 1
        # tmp = [0] * len(nums)
        # for idx, num in enumerate(nums):
        #     tmp[(idx + k) % len(nums)] = num
        # for idx, num in enumerate(tmp):
        #     nums[idx] = num

        # solution 2
        # l = len(nums)
        # n = 0
        #
        # i, tmp = 0, nums[0]
        # first = i
        # while True:
        #     next_i = (i + k) % l
        #     nums[next_i], tmp = tmp, nums[next_i]
        #     i = next_i
        #     n += 1
        #     if n == l:
        #         break
        #     elif i == first:
        #         i += 1
        #         tmp = nums[i]
        #         first = i
        # solution 3
        k = k % len(nums)
        for i in range(len(nums) // 2):
            nums[i], nums[-1 - i] = nums[-1 - i], nums[i]

        for i in range(k // 2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]

        for i in range((len(nums) - k) // 2):
            nums[k + i], nums[-1 - i] = nums[-1 - i], nums[k + i]

        print(nums)
        # return nums


solution = Solution().rotate

solution([1, 2, 3, 4, 5, 6], 4)
solution([-1, -100, 3, 99], 2)

solution([1, 2], 3)
solution([-1], 2)
