import sys

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
        # 1, < 2, die
        # 1, = 2 | 3, live
        # 1, > 3, die
        # 0, = 3, live
        neighbours = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                live = 0
                for x, y in neighbours:
                    if 0 <= i + x < m and 0 <= j + y < n and board[i + x][j + y] >= 1:
                        live += 1
                if board[i][j] == 0 and live == 3:
                    board[i][j] = -1  # 0 -> 1
                elif board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 2  # 1 -> 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == -1:
                    board[i][j] = 1
        return board


solution = Solution().gameOfLife
solution(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
solution(board=[[1, 1], [1, 0]])
