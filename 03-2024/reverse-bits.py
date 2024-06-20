import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def reverseBits(self, n):
        ret = 0
        offset = 0
        while offset < 32:
            ret = ret << 1
            ret += n % 2
            n = n >> 1
            offset += 1
        return ret


solution = Solution().reverseBits
solution(n=5)
