class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        matrix = [[int(x) for x in row] for row in matrix]
        if len(matrix) == 0:
            return 0
        max_v = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i == 0 or j == 0:
                    max_v = max(max_v, (matrix[i][j]))
                elif (matrix[i][j]) == 1:
                    matrix[i][j] = min(
                        (matrix[i-1][j-1]), (matrix[i][j-1]), (matrix[i-1][j])) + 1
                    max_v = max(max_v, matrix[i][j])
                else:
                    matrix[i][j] = 0
        return max_v*max_v


Solution().maximalSquare([['1']])
