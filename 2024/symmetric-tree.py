import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            elif dfs(node1.left, node2.right) and dfs(node1.right, node2.left):
                return True
            else:
                return False

        return dfs(root, root)


solution = Solution().isSymmetric
solution(root=stringToTreeNode("[1,2,2,3,4,4,3]"))
solution(root=stringToTreeNode("[1,2,2,null,3,null,3]"))
