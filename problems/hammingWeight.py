from tools import *


class Solution(object):
    @print_
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n:
            ret += n % 2
            n >>= 1
        return ret


solution = Solution().hammingWeight

solution(11)
solution(4294967293)