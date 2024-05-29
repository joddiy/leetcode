import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        map_ = {v: k for k, v in enumerate(inorder)}

        def construct(i, j):
            if j <= i:
                return None
            val = postorder.pop(-1)
            idx = map_[val]
            node = TreeNode(val)
            node.left = construct(i, idx)
            node.right = construct(idx + 1, j)
            return node

        return construct(0, len(inorder))


solution = Solution().buildTree
solution(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
