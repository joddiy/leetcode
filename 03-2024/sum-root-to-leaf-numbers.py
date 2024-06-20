import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(node, val):
            if not node.left and not node.right:
                return val * 10 + node.val
            elif not node.left:
                return dfs(node.right, val * 10 + node.val)
            elif not node.right:
                return dfs(node.left, val * 10 + node.val)
            else:
                return dfs(node.left, val * 10 + node.val) + dfs(node.right, val * 10 + node.val)

        return dfs(root, 0)


solution = Solution().sumNumbers
solution(root=stringToTreeNode("[1,2,3]"))
solution(root=stringToTreeNode("[4,9,0,5,1]"))
solution(root=stringToTreeNode("[]"))
solution(root=stringToTreeNode("[4,9,0,null,1]"))
