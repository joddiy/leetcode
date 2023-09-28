from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        bit = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            d_ = digits[i]
            digits[i] = (d_ + bit) % 10
            bit = (d_ + bit) // 10
        if bit == 1:
            digits.insert(0, 1)
        return digits


solution = Solution().plusOne
solution([4, 3, 2, 1])
solution([4, 3, 2, 9])
solution([9])
