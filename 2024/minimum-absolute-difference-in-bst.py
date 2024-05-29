import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node.left and not node.right:
                return node.val, node.val, sys.maxsize
            elif not node.left:
                r_s, r_l, r_m = dfs(node.right)
                return node.val, r_l, min(r_m, r_s - node.val)
            elif not node.right:
                l_s, l_l, l_m = dfs(node.left)
                return l_s, node.val, min(l_m, node.val - l_l)
            else:
                r_s, r_l, r_m = dfs(node.right)
                l_s, l_l, l_m = dfs(node.left)
                return l_s, r_l, min(r_m, l_m, node.val - l_l, r_s - node.val)

        _, _, ret = dfs(root)
        return ret


solution = Solution().getMinimumDifference
solution(root=stringToTreeNode("[4,2,6,1,3]"))
solution(root=stringToTreeNode("[1,0,48,null,null,12,49]"))
solution(root=stringToTreeNode("[1,null,3,2]"))
