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
        def recusive(root, upper, low):
            if not root:
                return True
            elif low < root.val < upper and recusive(
                    root.left, root.val, low) and recusive(
                        root.right, upper, root.val):
                return True
            else:
                return False

        return recusive(root, sys.maxsize, -sys.maxsize)


solution = Solution().isValidBST

solution("[]")
solution("[2,1,3]")
solution("[5,1,4,null,null,3,6]")
