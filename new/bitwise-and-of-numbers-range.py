import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # solution 1
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

        # slution 2
        # right_b = bin(right)[2:]
        # left_b = bin(left)[2:]
        # left_b = "0" * (len(right_b) - len(left_b)) + left_b
        #
        # def complement(bit_str):
        #     return int("".join(["0" if ch == "1" else "1" for ch in bit_str]), 2)
        #
        # left_sum = [1]
        # for i in range(len(left_b) - 2, -1, -1):
        #     if left_b[i] == "0":
        #         tmp = complement(left_b[i + 1:]) + 1
        #     else:
        #         tmp = complement(left_b[i:]) + 1
        #     left_sum.append(tmp)
        #
        # ret = []
        # diff = right - left
        # for i, n in enumerate(left_sum):
        #     if n <= diff:
        #         ret.insert(0, "0")
        #     else:
        #         ret.insert(0, left_b[len(left_b) - 1 - i])
        #
        # return int("".join(ret), 2)


solution = Solution().rangeBitwiseAnd
solution(left=5, right=7)
solution(left=0, right=0)
solution(left=1, right=2147483647)
# solution(left=1, right=7)
