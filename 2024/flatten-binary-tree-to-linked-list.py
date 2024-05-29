import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        def dfs(node):
            if node.left and node.right:
                l_h, l_e = dfs(node.left)
                r_h, r_e = dfs(node.right)
                node.left = None
                node.right = l_h
                l_e.right = r_h
                return node, r_e
            elif node.left:
                l_h, l_e = dfs(node.left)
                node.left = None
                node.right = l_h
                return node, l_e
            elif node.right:
                r_h, r_e = dfs(node.right)
                return node, r_e
            else:
                return node, node

        root, _ = dfs(root)
        return root


solution = Solution().flatten
# solution(root=stringToTreeNode("[1,2,5,3,4,null,6]"))
# solution(root=stringToTreeNode("[]"))
solution(root=stringToTreeNode("[1,2]"))
