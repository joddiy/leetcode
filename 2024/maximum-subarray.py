import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """


solution = Solution().snakesAndLadders
solution(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
solution(nums=[1])
solution(nums=[5, 4, -1, 7, 8])
