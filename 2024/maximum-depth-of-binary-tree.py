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

        def dfs(root):
            if not root:
                return 0
            else:
                l = dfs(root.left)
                r = dfs(root.right)
                return max(l, r) + 1

        return dfs(root)


solution = Solution().maxDepth
solution(root=stringToTreeNode("[3,9,20,null,null,15,7]"))
solution(root=stringToTreeNode("[1,null,2]"))
