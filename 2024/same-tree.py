import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif (not node1) or (not node2):
                return False
            elif node1.val != node2.val:
                return False
            else:
                if dfs(node1.left, node2.left) and dfs(node1.right, node2.right):
                    return True
                else:
                    return False

        return dfs(p, q)


solution = Solution().isSameTree
solution(p=stringToTreeNode("[1,2,3]"), q=stringToTreeNode("[1,2,3]"))
solution(p=stringToTreeNode("[1,2]"), q=stringToTreeNode("[1,null,2]"))
solution(p=stringToTreeNode("[1,2,1]"), q=stringToTreeNode("[1,1,2]"))
