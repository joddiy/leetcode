import sys

from tools import *
import pprint
from collections import Counter


class Solution(object):
    @print_
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while True:
            if n in visited:
                return False
            visited.add(n)
            if n == 1:
                return True
            cur = 0
            while n > 0:
                cur += (n % 10) ** 2
                n = n // 10
            n = cur


solution = Solution().isHappy
solution(n=19)
solution(n=2)
