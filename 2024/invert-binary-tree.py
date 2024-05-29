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

        def reverse(node):
            if node:
                node.left, node.right = reverse(node.right), reverse(node.left)
            return node

        return reverse(root)


solution = Solution().invertTree
solution(root=stringToTreeNode("[4,2,7,1,3,6,9]"))
solution(root=stringToTreeNode("[2,1,3]"))
