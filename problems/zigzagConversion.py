from tools import *


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

        res = ["" for i in range(numRows)]
        for idx, c in enumerate(s):
            local_idx = idx % (numRows * 2 - 2)
            if local_idx >= numRows:
                # 0, 1, 2, 3, 4 -> 2/-2, 5 -> 1/-3
                local_idx = -2 - (local_idx - numRows)
            res[local_idx] += c
        return "".join(res)


solution = Solution().convert

solution("A", 1)
solution("PAYPALISHIRING", 3)
solution("PAYPALISHIRING", 4)
