import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        index_map = {v: k for k, v in enumerate(inorder)}

        def build(postorder, index_l, index_r):
            if not postorder or index_l == index_r:
                return None
            value = postorder.pop()
            root = TreeNode(value)
            index = index_map[value]
            root.right = build(postorder, index + 1, index_r)
            root.left = build(postorder, index_l, index)
            return root

        return build(postorder, 0, len(inorder))


solution = Solution().buildTree
print(treeNodeToString(solution(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])))
