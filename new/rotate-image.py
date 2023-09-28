from tools import *
import pprint


class Solution(object):
    @print_
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # switch
        for i in range(len(matrix) // 2):
            matrix[i], matrix[len(matrix) - 1 - i] = matrix[len(matrix) - 1 - i], matrix[i]
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


solution = Solution().rotate
solution(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
