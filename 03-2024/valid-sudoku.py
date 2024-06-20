import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        idx_array = []
        offset_array = []
        for i in range(3):
            for j in range(3):
                idx_array.append((i, j))
                offset_array.append((i * 3, j * 3))
        for i in range(9):
            # cell
            off_i, off_j = offset_array[i]
            cur_ = set()
            for x, y in idx_array:
                num_ = board[off_i + x][off_j + y]
                if num_ in cur_:
                    return False
                if num_ != '.':
                    cur_.add(num_)
            # row
            cur_ = set()
            for j in range(9):
                num_ = board[i][j]
                if num_ in cur_:
                    return False
                if num_ != '.':
                    cur_.add(num_)
            # col
            cur_ = set()
            for j in range(9):
                num_ = board[j][i]
                if num_ in cur_:
                    return False
                if num_ != '.':
                    cur_.add(num_)
        return True


solution = Solution().isValidSudoku
solution(board=
         [["5", "3", ".", ".", "7", ".", ".", ".", "."]
             , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
             , [".", "9", "8", ".", ".", ".", ".", "6", "."]
             , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
             , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
             , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
             , [".", "6", ".", ".", ".", ".", "2", "8", "."]
             , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
             , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
solution(board=
         [["8", "3", ".", ".", "7", ".", ".", ".", "."]
             , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
             , [".", "9", "8", ".", ".", ".", ".", "6", "."]
             , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
             , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
             , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
             , [".", "6", ".", ".", ".", ".", "2", "8", "."]
             , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
             , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
