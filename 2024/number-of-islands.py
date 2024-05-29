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
        pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    array = [(i, j)]
                    while array:
                        i_, j_ = array.pop(0)
                        if 0 <= i_ < m and 0 <= j_ < n:
                            if grid[i_][j_] == '1':
                                for x, y in pos:
                                    array.append((i_ + x, j_ + y))
                            grid[i_][j_] = '0'
                    ret += 1
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
