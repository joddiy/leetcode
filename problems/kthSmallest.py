from tools import *


class Solution(object):
    @print_
    @tree_node
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.right, node.val, node.left])
            elif isinstance(node, int):
                k -= 1
                if k == 0:
                    return node

    @print_
    @tree_node
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.ret = None
        self.k = k
        def dfs(node):
            if self.k <= 0 or not node:
                return
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.ret = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.ret


solution = Solution().kthSmallest

solution("[3,1,4,null,2]", 1)
solution("[5,3,6,2,4,null,null,1]", 3)
solution("[3]", 1)
