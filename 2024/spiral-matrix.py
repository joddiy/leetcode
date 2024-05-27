import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        offset_map = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j, k, t = 0, 0, 0, 0
        x, y = offset_map[t]
        ret = []
        while True:
            ret.append(matrix[i][j])
            matrix[i][j] = 101
            if k == m * n - 1:
                return ret
            elif i + x < 0 or j + y < 0 or i + x >= m or j + y >= n or matrix[i + x][j + y] == 101:
                t = (t + 1) % 4
                x, y = offset_map[t]
            i += x
            j += y
            k += 1


solution = Solution().spiralOrder
solution(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
solution(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
solution(matrix=[[1]])
