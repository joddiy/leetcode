from tools import *
import sys


class Solution(object):
    @print_
    @tree_node
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = -sys.maxsize

        def dfs(root):
            if not root:
                return 0
            sum_l, sum_r = dfs(root.left), dfs(root.right)
            self.ret = max(self.ret, root.val + sum_l + sum_r)
            return max(root.val + sum_l, root.val + sum_r, 0)

        dfs(root)

        return self.ret


solution = Solution().maxPathSum

solution("[1,2,3]")
solution("[1,2,-3]")
solution("[-10,9,20,null,null,15,7]")
solution("[-3]")