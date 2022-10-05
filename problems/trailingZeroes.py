from tools import *


class Solution(object):
    @print_
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n:
            n //= 5
            ret += n
        return ret


solution = Solution().trailingZeroes

solution(0)
solution(3)
solution(5)
solution(15)