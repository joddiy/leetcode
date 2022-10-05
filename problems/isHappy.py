from tools import *


class Solution(object):
    @print_
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set_ = set()
        while n != 1 and n not in set_:
            set_.add(n)
            n_ = 0
            while n:
                n_ += (n % 10)**2
                n = n // 10
            n = n_
        return n == 1


solution = Solution().isHappy

solution(19)