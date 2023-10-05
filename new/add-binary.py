import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        a = list(a)
        b = list(b)
        ret = []
        while a or b:
            sum_ = carry
            if a:
                sum_ += int(a.pop())
            if b:
                sum_ += int(b.pop())
            if sum_ > 1:
                sum_ -= 2
                carry = 1
            else:
                carry = 0
            ret.insert(0, sum_)

        if carry:
            ret.insert(0, carry)
        return "".join(str(x) for x in ret)


solution = Solution().addBinary
solution(a="11", b="1")
solution(a="1010", b="1011")
