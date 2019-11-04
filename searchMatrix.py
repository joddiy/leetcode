class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # if len(matrix) == 0 or len(matrix[0]) == 0:
        #     return False
        # i, j, n, m = 0, 0, len(matrix)-1,  len(matrix[0])-1
        # # idx = 0
        # while True:
        #     # if idx > 20:
        #     #     return
        #     # idx += 1
        #     # print(i, j, n, m)
        #     if i == n and j == m:
        #         if matrix[i][j] == target:
        #             return True
        #         else:
        #             return False
        #     if i > n or j > m:
        #         return False
        #     if matrix[i][m] == target or matrix[n][j] == target or matrix[i][m] == target or matrix[i][0] == target:
        #         return True
        #     if matrix[i][m] > target:
        #         m -= 1
        #     elif matrix[n][j] > target:
        #         n -= 1
        #     elif matrix[i][m] < target:
        #         i += 1
        #     elif matrix[i][0] < target:
        #         j += 1

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        l = len(matrix[0]) - 1
        for row in matrix:
            while l > 0 and row[l] > target:
                l = l - 1
            if row[l] == target:
                return True
        return False

Solution().searchMatrix([[1, 1]], 1)
