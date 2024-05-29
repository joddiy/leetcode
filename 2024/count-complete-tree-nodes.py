import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0
            else:
                return dfs(node.left) + dfs(node.right) + 1

        return dfs(root)


solution = Solution().countNodes
solution(root=stringToTreeNode("[1,2,3,4,5,6]"))
solution(root=stringToTreeNode("[]"))
solution(root=stringToTreeNode("[1]"))
