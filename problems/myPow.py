from tools import *


class Solution(object):
    @print_
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            sign = -1
            n = -n
        else:
            sign = 1
        res = n % 2
        half = solutin(x, n // 2)
        ret = half * half if res == 0 else half * half * x
        if sign < 0:
            ret = 1 / ret
        return ret

    @print_
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        negative = (n < 0)
        n = abs(n)

        def recusive(i):
            if i == 0:
                return 1
            if i == 1:
                return x
            t = recusive(i // 2)
            if i % 2:
                return t * t * x
            else:
                return t * t

        ret = recusive(n)
        return 1 / ret if negative else ret


solution = Solution().myPow
solution(2., 10)
solution(2., 2)
solution(2., -2)
solution(2., 0)