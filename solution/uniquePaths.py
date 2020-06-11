class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        rst = 1
        for i in range(n-1, 0, -1):
            rst *= m
            m += 1
            rst /= i
        return int(round(rst))

    #case 2
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        # Create a empty mxn matrix
        matrix = [[1]*n for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

        return (matrix[m-1][n-1])


print(Solution().uniquePaths(10, 10))
