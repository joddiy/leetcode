from tools import *
import sys


class Solution(object):
    @print_
    @tree_node
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(root, low, high):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return valid(root.left, low, root.val) and valid(
                root.right, root.val, high)

        return valid(root, -sys.maxsize, sys.maxsize)


solution = Solution().isValidBST

solution("[]")
solution("[2,1,3]")
solution("[5,1,4,null,null,3,6]")
