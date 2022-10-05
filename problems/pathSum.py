from tools import *


class Solution(object):
    @print_
    @tree_node
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.ret = 0
        memo = {0: 1}

        def dfs(root, cur_sum):
            if not root:
                return

            cur_sum += root.val
            self.ret += memo.get(cur_sum - sum, 0)
            memo[cur_sum] = memo.get(cur_sum, 0) + 1
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            memo[cur_sum] -= 1

        dfs(root, 0)
        return self.ret


solution = Solution().pathSum

solution("[10,5,-3,3,2,null,11,3,-2,null,1]", 8)