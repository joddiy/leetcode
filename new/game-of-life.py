from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


solution = Solution().gameOfLife
solution(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
