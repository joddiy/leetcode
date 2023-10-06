import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        int_list = []
        while x:
            int_list.append(x % 10)
            x = x // 10

        for i in range(len(int_list) // 2):
            if int_list[i] != int_list[-i - 1]:
                return False
        return True


solution = Solution().isPalindrome
# solution(x=121)
# solution(x=-121)
# solution(x=10)
solution(x=1000021)
