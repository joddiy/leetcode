import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)
        if n == 0:
            return None

        def build(x1, x2, y1, y2):
            if x1 == x2 and y1 == y2:
                node = Node(grid[x1][y1])
                node.isLeaf = True
            else:
                node = Node()
                x_m = (x1 + x2) // 2
                y_m = (y1 + y2) // 2
                tl = build(x1, x_m, y1, y_m)
                tr = build(x1, x_m, y_m + 1, y2)
                bl = build(x_m + 1, x2, y1, y_m)
                br = build(x_m + 1, x2, y_m + 1, y2)
                if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and (tl.val == tr.val == bl.val == br.val):
                    node.val = tl.val
                    node.isLeaf = True
                    del tl, tr, bl, br
                else:
                    node.topLeft = tl
                    node.topRight = tr
                    node.bottomLeft = bl
                    node.bottomRight = br
            return node

        return build(0, n - 1, 0, n - 1)


solution = Solution().construct
# solution(grid=[[0, 1], [1, 0]])
solution(grid=[[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]])
