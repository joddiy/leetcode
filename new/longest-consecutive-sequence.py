import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        max_l = 0
        for n in nums:
            tmp_l = 0
            if n in nums_set:
                tmp_l += 1
                nums_set.remove(n)
                n_ = n
                while n_ - 1 in nums_set:
                    tmp_l += 1
                    nums_set.remove(n_ - 1)
                    n_ -= 1
                n_ = n
                while n_ + 1 in nums_set:
                    tmp_l += 1
                    nums_set.remove(n_ + 1)
                    n_ += 1
            max_l = max(max_l, tmp_l)
        return max_l


solution = Solution().longestConsecutive
solution(nums=[100, 4, 200, 1, 3, 2])
solution(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
solution(nums=[])
