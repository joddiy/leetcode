from tools import *


class Solution(object):
    @print_
    @tree_node
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ret = None

        def dfs(root):
            if self.ret is not None or not root:
                return False
            result = [dfs(root.left), dfs(root.right), root.val in (q, p)]
            if sum(result) == 2 and self.ret is None:
                self.ret = root.val
            return max(result)

        dfs(root)
        return self.ret


solution = Solution().lowestCommonAncestor
solution("[3,5,1,6,2,0,8,null,null,7,4]", 5, 1)
solution("[3,5,1,6,2,0,8,null,null,7,4]", 5, 4)
solution("[1,2]", 1, 2)