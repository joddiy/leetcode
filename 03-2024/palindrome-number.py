import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


solution = Solution().isPalindrome
solution(x=121)
solution(x=-121)
solution(x=10)
