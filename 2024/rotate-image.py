import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        for i in range(m // 2):
            matrix[i], matrix[m - i - 1] = matrix[m - i - 1], matrix[i]
        for i in range(m):
            for j in range(i + 1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


solution = Solution().rotate
solution(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
