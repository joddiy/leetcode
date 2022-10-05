from tools import *


class Solution(object):
    @print_
    @tree_node
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, 0
            lr, lnr = dfs(root.left)
            rr, rnr = dfs(root.right)
            r = lnr + rnr + root.val
            nr = max(lr, lnr) + max(rr, rnr)
            return r, nr

        return max(dfs(root))


solution = Solution().rob

solution("[3,2,3,null,3,null,1]")
solution("[3,4,5,1,3,null,1]")