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
        if not board or not board[0]:
            return board
        pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                sum_ = 0
                for r, c in pos:
                    i_ = i + r
                    j_ = j + c
                    if 0 <= i_ < m and 0 <= j_ < n and abs(board[i_][j_]) == 1:
                        sum_ += 1
                if board[i][j] == 0 and sum_ == 3:
                    # from 0 to 1
                    board[i][j] = 2
                if board[i][j] == 1 and (sum_ < 2 or sum_ > 3):
                    # from 1 to -1
                    board[i][j] = -1
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        return board


solution = Solution().gameOfLife
solution(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
solution(board=[])
