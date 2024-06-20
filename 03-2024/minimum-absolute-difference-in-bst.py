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

        self.ret = sys.maxsize
        self.pre = None

        def dfs(node):
            if not node:
                return
            else:
                dfs(node.left)
                if self.pre is not None:
                    self.ret = min(self.ret, node.val - self.pre)
                self.pre = node.val
                dfs(node.right)

        dfs(root)
        return self.ret


solution = Solution().getMinimumDifference
solution(root=stringToTreeNode("[4,2,6,1,3]"))
solution(root=stringToTreeNode("[1,0,48,null,null,12,49]"))
solution(root=stringToTreeNode("[1,null,3,2]"))
