import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])

        def find(i, j):
            if i > j:
                return False
            else:
                k = (i + j) // 2
                x = k // n
                y = k % n
                if target == matrix[x][y]:
                    return True
                elif target > matrix[x][y]:
                    return find(k + 1, j)
                else:
                    return find(i, k - 1)

        return find(0, m * n - 1)


solution = Solution().searchMatrix
solution(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
solution(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)
