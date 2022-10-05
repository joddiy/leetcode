from tools import *
import math


class Solution(object):
    @print_
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return 0
        while n % 3 == 0:
            n = n // 3
        return True if n == 1 else False

    @print_
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0


solution = Solution().isPowerOfThree

solution(27)
