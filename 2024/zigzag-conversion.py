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
        ret = ["" for _ in range(numRows)]
        for i in range(len(s)):
            local_idx = i % (2 * numRows - 2)
            if local_idx >= numRows:
                local_idx = -(local_idx - numRows + 1) - 1
            ret[local_idx] += s[i]
        return "".join(ret)


solution = Solution().convert
# solution(s="PAYPALISHIRING", numRows=3)
# solution(s="PAYPALISHIRING", numRows=4)
solution(s="A", numRows=1)
solution(s="AN", numRows=1)
