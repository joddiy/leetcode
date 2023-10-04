import math
import pprint
import sys

from tools import *
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
        ll = len(word)
        pos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = [[0] * n for _ in range(m)]

        def recusive(i, j, k):
            if k == ll:
                return True
            elif i < 0 or i >= m or j < 0 or j >= n or visited[i][j] == 1:
                return False
            else:
                if board[i][j] == word[k]:
                    visited[i][j] = 1
                    for px, py in pos:
                        if recusive(i + px, j + py, k + 1):
                            return True
                    visited[i][j] = 0
                    return False
                else:
                    return False

        for i in range(m):
            for j in range(n):
                if recusive(i, j, 0):
                    return True
        return False


solution = Solution().exist
solution(board=[
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
], word="ABCCED")

solution(board=[
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
], word="SEE")

solution(board=[
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
], word="ABCB")
