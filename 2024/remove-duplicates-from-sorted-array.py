import sys

from tools import *
import pprint


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n:
            _val = nums.pop(0)
            if len(nums) < 1 or _val != nums[-1]:
                nums.append(_val)
            i += 1

        return len(nums)


solution = Solution().removeDuplicates
# solution(nums=[1, 1, 2])
# solution(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
solution(nums=[1])
solution(nums=[1, 1])
solution(nums=[])
