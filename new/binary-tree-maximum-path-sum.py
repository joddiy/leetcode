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
        self.ret = -sys.maxsize

        def recursive(node):
            if not node:
                return 0
            left = recursive(node.left)
            right = recursive(node.right)
            self.ret = max(self.ret, left + right + node.val)
            return max(left + node.val, right + node.val, 0)

        recursive(root)
        return self.ret


solution = Solution().maxPathSum
solution(root=stringToTreeNode("[1,2,3]"))
solution(root=stringToTreeNode("[-10,9,20,null,null,15,7]"))
