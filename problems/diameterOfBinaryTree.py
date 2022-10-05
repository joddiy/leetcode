from tools import *


class Solution(object):
    @print_
    @tree_node
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0

        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)
            self.ret = max(self.ret, l + r)
            return max(l, r) + 1

        dfs(root)
        return self.ret


solution = Solution().diameterOfBinaryTree
solution("[1,2,3,4,5]")