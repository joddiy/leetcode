import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        pos = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        def mark(i, j):
            if board[i][j] != 'O':
                return
            else:
                board[i][j] = 'S'
                for x, y in pos:
                    if 0 <= i + x < m and 0 <= j + y < n:
                        mark(i + x, j + y)

        for i in range(m):
            mark(i, 0)
            mark(n - 1, 0)

        for j in range(n):
            mark(0, j)
            mark(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return board


solution = Solution().solve
solution(board=[["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"]])
solution(board=[["X"]])
