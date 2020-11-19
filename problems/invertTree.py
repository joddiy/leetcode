from tools import *


class Solution(object):
    @print_
    @tree_node
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(root):
            if root:
                root.left, root.right = invert(root.right), invert(root.left)
            return root

        return invert(root)


solution = Solution().invertTree

solution("[4,2,7,1,3,6,9]")