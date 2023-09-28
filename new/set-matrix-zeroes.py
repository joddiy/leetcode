from tools import *
import pprint


class Solution(object):
    @print_
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # solution 1
        n, m = len(matrix), len(matrix[0])
        zero_r = [False] * n
        zero_c = [False] * m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_r[i] = True
                    zero_c[j] = True
        for i in range(n):
            for j in range(m):
                if zero_r[i] or zero_c[j]:
                    matrix[i][j] = 0
        return matrix


solution = Solution().setZeroes
# solution(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
solution(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
