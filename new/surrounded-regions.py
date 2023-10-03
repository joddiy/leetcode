import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
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
# solution(board=[
#     ["X", "X", "X", "X"],
#     ["X", "O", "O", "X"],
#     ["X", "X", "O", "X"],
#     ["X", "O", "X", "X"]
# ])

solution(board=[
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"]
])

# solution(board=[
#     ["X"]
# ])
