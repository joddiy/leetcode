import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()

        def local_sum(n):
            ret = 0
            while n > 0:
                ret += (n % 10) ** 2
                n //= 10
            return ret

        while True:
            if n == 1:
                return True
            elif n in visited:
                return False
            else:
                visited.add(n)
            n = local_sum(n)


solution = Solution().isHappy
solution(n=19)
solution(n=2)
