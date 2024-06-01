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
solution(board=[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]])
solution(board=[[-1, -1], [-1, 3]])
