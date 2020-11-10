from tools import *


class Solution(object):
    @print_
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        t = 32
        while n:
            ret <<= 1
            ret += n % 2
            n >>= 1
            t -= 1
        while t:
            ret <<= 1
            t -= 1
        return ret


solution = Solution().reverseBits

solution(2)
solution(11)
solution(43261596)
# solution(4294967293)
