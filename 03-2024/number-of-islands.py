import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])

        def remove(i, j):
            if grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                for x, y in pos:
                    if 0 <= i + x < m and 0 <= j + y < n:
                        remove(i + x, j + y)

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ret += 1
                    remove(i, j)
        return ret


solution = Solution().numIslands
# solution(grid=[
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ])
solution(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])
