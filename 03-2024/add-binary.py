import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = list(a), list(b)
        ret = []
        c = 0
        while a or b:
            if a:
                c += int(a.pop())
            if b:
                c += int(b.pop())
            ret.insert(0, c % 2)
            c //= 2
        if c != 0:
            ret.insert(0, c)
        return "".join(str(x) for x in ret)


solution = Solution().addBinary
solution(a="11", b="1")
solution(a="1010", b="1011")
