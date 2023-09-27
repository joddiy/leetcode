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
        # 0 -> (6) -> (n+2)
        # 1 -> (1+n=5) -> (1+n+2)
        # 2 -> (2+n-2=4) -> (2+n+2)
        # 3 -> (3) -> (3+n+2)
        if numRows == 1:
            return s
        max_n = len(s)
        offset = numRows * 2 - 2
        ret = ""
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                # only 1 output
                j = i
                while j < max_n:
                    ret += s[j]
                    j += offset
            else:
                # two output
                j = i
                while j < max_n:
                    ret += s[j]
                    tmp_j = j + offset - i * 2
                    if tmp_j < max_n:
                        ret += s[tmp_j]
                    j += offset
        return ret


solution = Solution().convert
# solution("PAYPALISHIRING", 3)
# solution("PAYPALISHIRING", 4)
# solution("A", 1)
solution("A", 2)
