import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        self.pos = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        def remove(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0"
                for x, y in self.pos:
                    remove(i + x, j + y)

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ret += 1
                    remove(i, j)
        return ret


solution = Solution().numIslands
solution(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
])
solution(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])
