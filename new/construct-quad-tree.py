import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
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
        m, n = len(grid), len(grid[0])

        def build(i, len_i, j, len_j):
            if len_j == 1 or len_j == 1:
                node = Node(grid[i][j], True, None, None, None, None)
                if node.val == 1:
                    return node, 0, 1
                else:
                    return node, 1, 0
            hlen_i = len_i // 2
            hlen_j = len_j // 2
            # topleft
            zero_n, one_n = 0, 0
            tl, tl_0, tl_1 = build(i, hlen_i, j, hlen_j)
            zero_n += tl_0
            one_n += tl_1
            # topright
            tr, tr_0, tr_1 = build(i, hlen_i, j + hlen_j, hlen_j)
            zero_n += tr_0
            one_n += tr_1
            # bottomleft
            bl, bl_0, bl_1 = build(i + hlen_i, hlen_i, j, hlen_j)
            zero_n += bl_0
            one_n += bl_1
            # bottomright
            br, br_0, br_1 = build(i + hlen_i, hlen_i, j + hlen_j, hlen_j)
            zero_n += br_0
            one_n += br_1
            if zero_n == 0:  # all subtree are ones
                node = Node(1, True, None, None, None, None)
            elif one_n == 0:  # all subtree are zeros
                node = Node(0, True, None, None, None, None)
            else:
                node = Node(1, False, tl, tr, bl, br)

            return node, zero_n, one_n

        root, _, _ = build(0, m, 0, n)
        return root


solution = Solution().construct
solution(grid=[[0, 1], [1, 0]])
