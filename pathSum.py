from utils.tools import *


class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def recursive(root, target, currPathSum, cache):
            if root:
                # calculate currPathSum and required oldPathSum
                currPathSum += root.val
                oldPathsum = currPathSum - target
                # update result and cache
                self.result += cache.get(oldPathsum, 0)
                cache[currPathSum] = cache.get(currPathSum, 0) + 1

                # dfs breakdown
                recursive(root.left, target, currPathSum, cache)
                recursive(root.right, target, currPathSum, cache)
                # when move to a different branch, the currPathSum is no longer available, hence remove one. 
                cache[currPathSum] -= 1

        self.result = 0
        cache = {0: 1}
        recursive(root, target, 0, cache)
        return self.result


print(Solution().pathSum(stringToTreeNode(
    "[10,5,-3,3,2,null,11,3,-2,null,1]"), 8))
