from tools import *


class Solution(object):
    # space O(m + n)
    @print_
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows = set()
        columns = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in columns:
                    matrix[i][j] = 0

        return matrix

    # space O(1)
    # using the first cell to mark
    @print_
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # we mark first col and row by these two labels
        # because we must use the first col and row later
        first_col, first_row = False, False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_col:
            for i in range(m):
                matrix[i][0] = 0

        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        return matrix


solution = Solution().setZeroes

# solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
# solution([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
solution([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]])
