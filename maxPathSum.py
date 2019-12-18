from utils.tools import *
import sys


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # greedy search is ok for non-negative values
        def recursive(root):
            if root:
                left_max_0, right_max_0, max_path_0 = recursive(
                    root.left)
                left_max_1, right_max_1, max_path_1 = recursive(
                    root.right)
                left_max = max(left_max_0, right_max_0)
                right_max = max(left_max_1, right_max_1)
                return left_max + root.val, right_max + root.val, left_max + right_max + root.val
            else:
                return 0, 0, 0
        _, _, res = recursive(root)
        return res

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left is None and root.right is None:
            return root.val
        self.res = -sys.maxsize

        def recursive(root):
            if root:
                left_max = recursive(root.left)
                right_max = recursive(root.right)
                self.res = max(self.res, left_max + right_max + root.val)
                return max(left_max + root.val, right_max + root.val, 0)
            else:
                return 0
        recursive(root)
        return self.res


print(Solution().maxPathSum(stringToTreeNode('[1,2,3]')))
print(Solution().maxPathSum(stringToTreeNode('[-10,9,20,null,null,15,7]')))
print(Solution().maxPathSum(stringToTreeNode('[-3]')))
print(Solution().maxPathSum(stringToTreeNode('[2,-1]')))
