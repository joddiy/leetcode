import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0
            else:
                return max(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)


solution = Solution().maxDepth
solution(root=stringToTreeNode("[3,9,20,null,null,15,7]"))
solution(root=stringToTreeNode("[1,null,2]"))
