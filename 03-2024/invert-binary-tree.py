import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if node:
                node.left, node.right = dfs(node.right), dfs(node.left)
            return node

        return dfs(root)


solution = Solution().invertTree
solution(root=stringToTreeNode("[4,2,7,1,3,6,9]"))
solution(root=stringToTreeNode("[2,1,3]"))
