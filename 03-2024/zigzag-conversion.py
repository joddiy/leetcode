import math
import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ret = [[] for _ in range(numRows)]
        offset = [1] * (numRows - 1) + [-1] * (numRows - 1)

        i = 0
        j = 0
        for c in s:
            ret[i].append(c)
            i = i + offset[j]
            j = (j + 1) % len(offset)

        return "".join("".join(r) for r in ret)


solution = Solution().convert
solution(s="PAYPALISHIRING", numRows=3)
# solution(s="PAYPALISHIRING", numRows=4)
# solution(s="A", numRows=1)
# solution(s="AN", numRows=1)
