from tools import *


class Solution(object):
    @print_
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        ret = []
        for i in range(numRows):
            if i <= len(ret):
                ret.append([1])
            for j in range(1, i + 1):
                if j == i:
                    ret[i].append(1)
                else:
                    ret[i].append(ret[i - 1][j - 1] + ret[i - 1][j])
        return ret


solution = Solution().generate

solution(5)