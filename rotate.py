class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        # reverse
        for i in range(0, h//2, 1):
            matrix[i], matrix[h-i-1] = matrix[h-i-1], matrix[i]
        # transpose
        for i in range(0, h, 1):
            for j in range(0, i, 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

Solution().rotate(matrix)
