import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ret = []
        cur = 1
        while digits:
            cur += digits.pop()
            ret.insert(0, cur % 10)
            cur = cur // 10
        if cur:
            ret.insert(0, cur)
        return ret


solution = Solution().plusOne
solution(digits=[1, 2, 3])
solution(digits=[4, 3, 2, 1])
solution(digits=[9])
