import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution 1, n^2
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # solution 2, nlogn
        def bisect(arr, num):
            # O(n), can optimize to O(logn)
            for i in range(0, len(arr)):
                if arr[i] >= num:
                    return i
            return len(arr)

        ans = [nums.pop(0)]

        for num in nums:
            if num > ans[-1]:
                ans.append(num)
            else:
                i = bisect(ans, num)
                ans[i] = num

        return len(ans)




solution = Solution().lengthOfLIS
solution(nums=[10, 9, 2, 5, 3, 7, 1, 18])
# solution(nums=[0, 1, 0, 3, 2, 3])
# solution(nums=[7, 7, 7, 7, 7, 7, 7])
# solution(nums=[1, 3, 6, 7, 9, 4, 10, 5, 6])
