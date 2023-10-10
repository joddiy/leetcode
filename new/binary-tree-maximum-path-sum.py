import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_ret = -sys.maxsize

        def recursive(node):
            if not node:
                return 0
            l = recursive(node.left)
            r = recursive(node.right)
            self.max_ret = max(self.max_ret, l + r + node.val)
            return max(l + node.val, r + node.val, 0)

        recursive(root)
        return self.max_ret


solution = Solution().maxPathSum
solution(root=stringToTreeNode("[1,2,3]"))
solution(root=stringToTreeNode("[-10,9,20,null,null,15,7]"))
