import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.ret = None

        # k means, find the kth smallest in the current sub-tree
        # the return value means, the total number of node for the current sub-tree
        def recursive(root, k):
            if not root:
                return 0
            left = recursive(root.left, k)
            if left + 1 == k:
                self.ret = root.val
            right = recursive(root.right, k - left - 1)
            return left + right + 1

        recursive(root, k)
        return self.ret


solution = Solution().kthSmallest
print(solution(stringToTreeNode("[3,1,4,null,2]"), k=1))
print(solution(stringToTreeNode("[5,3,6,2,4,null,null,1]"), k=3))
