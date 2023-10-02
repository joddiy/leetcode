import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        index_map = {v: k for k, v in enumerate(inorder)}

        def build(preorder, index_l, index_r):
            if not preorder or index_l == index_r:
                return None
            value = preorder.pop(0)
            root = TreeNode(value)
            index = index_map[value]
            root.left = build(preorder, index_l, index)
            root.right = build(preorder, index + 1, index_r)
            return root

        return build(preorder, 0, len(inorder))


solution = Solution().buildTree
print(treeNodeToString(solution(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])))
