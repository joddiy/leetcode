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
        # pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # m, n = len(board), len(board[0])
        # visited = [[0 for _ in range(n)] for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O':
        #             array = [(i, j)]
        #             all_array = []
        #             flip = True
        #             while array:
        #                 i_, j_ = array.pop(0)
        #                 if (0 <= i_ < m) and (0 <= j_ < n):
        #                     if visited[i_][j_] == 0 and board[i_][j_] == 'O':
        #                         all_array.append((i_, j_))
        #                         for x, y in pos:
        #                             array.append((i_ + x, j_ + y))
        #                     visited[i_][j_] = 1
        #                 else:
        #                     flip = False
        #             if flip:
        #                 for i_, j_ in all_array:
        #                     board[i_][j_] = 'X'
        # return board

        m, n = len(board), len(board[0])
        self.pos = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        def mark(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != "O":
                return
            else:
                board[i][j] = "S"
                for x, y in self.pos:
                    mark(i + x, j + y)

        for i in range(m):
            if board[i][0] == "O":
                mark(i, 0)
            if board[i][n - 1] == "O":
                mark(i, n - 1)

        for j in range(n):
            if board[0][j] == "O":
                mark(0, j)
            if board[m - 1][j] == "O":
                mark(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        print(board)


solution = Solution().solve
solution(board=[["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"]])
solution(board=[["X"]])
