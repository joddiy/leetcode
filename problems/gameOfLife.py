from tools import *


class Solution(object):
    @print_
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        board_copy = [[i for i in j] for j in board]
        pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
               (1, 1)]
        for i in range(n):
            for j in range(m):
                sum_ = 0
                for l, r in pos:
                    i_, j_ = i + l, j + r
                    if 0 <= i_ < n and 0 <= j_ < m and board_copy[i_][j_] == 1:
                        sum_ += 1
                if board[i][j] == 1 and (sum_ < 2 or sum_ > 3):
                    board[i][j] = 0
                elif board[i][j] == 0 and sum_ == 3:
                    board[i][j] = 1

        return board

    @print_
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
               (1, 1)]
        for i in range(n):
            for j in range(m):
                sum_ = 0
                for l, r in pos:
                    i_, j_ = i + l, j + r
                    # abs only count -1 and 1
                    if 0 <= i_ < n and 0 <= j_ < m and abs(board[i_][j_]) == 1:
                        sum_ += 1
                if board[i][j] == 1 and (sum_ < 2 or sum_ > 3):
                    # -1 signifies the cell is now dead but originally was live.
                    board[i][j] = -1
                elif board[i][j] == 0 and sum_ == 3:
                    # 2 signifies the cell is now live but was originally dead.
                    board[i][j] = 2

        for i in range(n):
            for j in range(m):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        return board


solution = Solution().gameOfLife

solution([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
