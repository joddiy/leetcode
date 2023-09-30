import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and root.right:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        elif root.left:
            return self.maxDepth(root.left) + 1
        elif root.right:
            return self.maxDepth(root.right) + 1


solution = Solution().maxDepth
print(solution(root=stringToTreeNode("[3,9,20,null,null,15,7]")))
