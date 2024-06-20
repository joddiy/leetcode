import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node:
                return None, 0
            else:
                l, l_n = dfs(node.left)
                if l_n == 2:
                    return l, 2
                r, r_n = dfs(node.right)
                if r_n == 2:
                    return r, 2
                if l_n + r_n == 2:
                    return node, 2
                if node is p or node is q:
                # if node.val in (p, q):
                    return node, l_n + r_n + 1
                return None, l_n + r_n

        node, _ = dfs(root)
        return node


solution = Solution().lowestCommonAncestor
solution(root=stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"), p=5, q=1)
solution(root=stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"), p=5, q=4)
