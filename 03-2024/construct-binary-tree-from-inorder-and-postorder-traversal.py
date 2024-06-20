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
        map_ = {v: i for i, v in enumerate(inorder)}

        def build(i, j):
            if j < i:
                return None
            else:
                val = postorder.pop()
                idx = map_[val]
                node = TreeNode(val)
                node.right = build(idx + 1, j)
                node.left = build(i, idx - 1)
                return node

        return build(0, len(postorder) - 1)


solution = Solution().buildTree
solution(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
