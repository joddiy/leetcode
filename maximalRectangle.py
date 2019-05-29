from utils.tools import *


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = [[[0, 0] for x in row] for row in matrix]  # (row,col)
        if len(dp) == 0:
            return 0
        max_v = 0
        if matrix[0][0] == '1':
            dp[0][0] = [1, 1]
            max_v = 1
        for i in range(1, len(matrix)):
            if matrix[i][0] == '1':
                dp[i][0][1] += dp[i-1][0][1]
            dp[i][0][0] = dp[i-1][0][0]
            max_v = max(max_v, dp[i][0][0] * dp[i][0][1])
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == '1':
                dp[0][j][0] += dp[0][j-1][0]
            dp[0][j][1] = dp[0][j-1][1]
            max_v = max(max_v, dp[0][j][0] * dp[0][j][1])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if (matrix[i][j]) == '1':
                    dp[i][j][1] += dp[i-1][j][1]
                    dp[i][j][0] += dp[i][j-1][0]
                    max_v = max(max_v, dp[i][j][0] * dp[i][j][1])
        print_array(dp)
        return max_v


Solution().maximalRectangle([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
])
