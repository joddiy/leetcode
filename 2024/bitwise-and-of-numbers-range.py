import math
import pprint
import sys

from tools import *
from collections import defaultdict
import heapq


class Solution(object):
    @print_
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


solution = Solution().rangeBitwiseAnd
solution(left=5, right=7)
# solution(left=0, right=0)
# solution(left=1, right=2147483647)
