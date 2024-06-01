import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(32):
            sum_ = 0
            for n in nums:
                if n < 0:
                    n = n & (2 ** 32 - 1)
                sum_ += (n >> i) % 2
            sum_ %= 3
            ret += sum_ << i

        if ret >= 2 ** 31:
            ret -= 2 ** 32
        return ret


solution = Solution().singleNumber
# solution(nums=[2, 2, 3, 2])
# solution(nums=[0, 1, 0, 1, 0, 1, 99])
solution(nums=[-2, -2, 1, 1, 4, 1, 4, 4, -4, -2])
