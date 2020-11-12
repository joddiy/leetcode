from tools import *


class Solution(object):
    @print_
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ret = 0
        n, m = len(grid), len(grid[0])

        # dfs
        def mark(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == '0':
                return
            else:
                grid[i][j] = '0'
                mark(i + 1, j)
                mark(i, j + 1)
                mark(i - 1, j)
                mark(i, j - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ret += 1
                    mark(i, j)

        return ret


solution = Solution().numIslands

solution([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])

solution([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])

solution([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]])

