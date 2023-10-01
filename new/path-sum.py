import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        elif root.left is not None and root.right is not None:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        elif root.left is not None:
            return self.hasPathSum(root.left, targetSum - root.val)
        elif root.right is not None:
            return self.hasPathSum(root.right, targetSum - root.val)


solution = Solution().hasPathSum
print(solution(stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,null,1]"), targetSum=22))
print(solution(stringToTreeNode("[1,2,3]"), targetSum=5))
print(solution(stringToTreeNode("[]"), targetSum=0))
