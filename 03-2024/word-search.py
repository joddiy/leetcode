import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def find(i, j, k):
            if board[i][j] != word[k]:
                return False
            elif k == len(word) - 1:
                return True
            else:
                board[i][j] = '#'
                ret = False
                for x, y in pos:
                    if 0 <= x + i < m and 0 <= y + j < n:
                        if find(x + i, y + j, k + 1):
                            ret = True
                            break
                board[i][j] = word[k]
                return ret

        for i in range(m):
            for j in range(n):
                if find(i, j, 0):
                    return True
        return False


solution = Solution().exist
solution(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
# solution(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE")
# solution(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB")
