import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


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
            if j < i:
                return False
            mid = (i + j) // 2
            mid_ = matrix[mid // n][mid % n]
            if mid_ == target:
                return True
            elif mid_ < target:
                return find(mid + 1, j)
            else:
                return find(i, mid - 1)

        return find(0, m * n - 1)


solution = Solution().searchMatrix
solution(matrix=[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
], target=3)
solution(matrix=[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
], target=13)
