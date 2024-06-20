import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        def dfs(node, t):
            if not node.left and not node.right:
                return t == node.val
            elif not node.left:
                return dfs(node.right, t - node.val)
            elif not node.right:
                return dfs(node.left, t - node.val)
            else:
                return dfs(node.left, t - node.val) or dfs(node.right, t - node.val)

        return dfs(root, targetSum)


solution = Solution().hasPathSum
solution(root=stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,null,1]"), targetSum=22)
solution(root=stringToTreeNode("[1,2,3]"), targetSum=5)
solution(root=stringToTreeNode("[]"), targetSum=0)
solution(root=stringToTreeNode("[1,2]"), targetSum=1)
