import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        else:
            left, right = root.left, root.right
            root.left = self.invertTree(right)
            root.right = self.invertTree(left)
            return root


solution = Solution().invertTree
print(treeNodeToString(solution(stringToTreeNode("[4,2,7,1,3,6,9]"))))
