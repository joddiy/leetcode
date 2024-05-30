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
        visited = [[0 for _ in range(n)] for _ in range(m)]

        def find(i, j, k):
            if k == len(word):
                return True
            elif 0 <= i < m and 0 <= j < n and visited[i][j] != 1:
                visited[i][j] = 1
                if board[i][j] == word[k]:
                    for x, y in pos:
                        if find(i + x, j + y, k + 1):
                            return True
                visited[i][j] = 0
                return False

        for i in range(m):
            for j in range(n):
                if find(i, j, 0):
                    return True
        return False


solution = Solution().exist
solution(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
solution(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE")
solution(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB")
