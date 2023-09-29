from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        nums_map = defaultdict(int)
        for i, k in enumerate(nums):
            nums_map[k] = i
        ret = []
        last_i, last_j = None, None
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left_ = 0 - (nums[i] + nums[j])
                k = nums_map[left_]
                if k > i and k > j and (last_i != nums[i] or last_j != nums[j]):
                    ret.append([nums[i], nums[j], left_])
                    last_i = nums[i]
                    last_j = nums[j]
        return ret


solution = Solution().threeSum
solution(nums=[-1, 0, 1, 2, -1, -4])
solution(nums=[0, 0, 0, 0])
solution(nums=[-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
