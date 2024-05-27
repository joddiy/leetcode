import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        c_ = False
        for i in range(m):
            if matrix[i][0] == 0:
                c_ = True
                break

        r_ = False
        for i in range(n):
            if matrix[0][i] == 0:
                r_ = True
                break

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0

        if c_:
            for i in range(m):
                matrix[i][0] = 0
        if r_:
            for i in range(n):
                matrix[0][i] = 0
        return matrix


solution = Solution().setZeroes
# solution(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
# solution(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
solution(matrix=[[1], [0]])
