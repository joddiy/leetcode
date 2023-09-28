from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        offset = 0
        while offset < 32:
            ret <<= 1
            if n % 2 == 1:
                ret += 1
            n >>= 1
            offset += 1
        return ret


solution = Solution().reverseBits
solution(n=5)
# solution(n=7)
