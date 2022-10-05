from tools import *


class Solution(object):
    @print_
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def find(i, j):
            if j < i:
                return j
            m = (i + j) // 2
            m_ = m * m
            if m_ == x:
                return m
            elif m_ < x:
                return find(m + 1, j)
            else:
                return find(i, m - 1)

        return find(0, x)


solution = Solution().mySqrt

solution(0)
solution(1)
solution(4)
solution(8)
solution(9)
