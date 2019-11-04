from utils.tools import treeNodeToString, TreeNode, stringToTreeNode


class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def recursive(root, target, currPathSum, cache):
            if root:
                currPathSum += root.val
                oldPathsum = currPathSum - target
                self.result += cache.get(oldPathsum, 0)
                cache[currPathSum] = cache.get(currPathSum, 0) + 1

                print(root.val, currPathSum, oldPathsum, self.result, cache)
                recursive(root.left, target, currPathSum, cache)
                recursive(root.right, target, currPathSum, cache)
                cache[currPathSum] -= 1

        self.result = 0
        cache = {0: 1}
        recursive(root, target, 0, cache)
        return self.result


print(Solution().pathSum(stringToTreeNode("[10,5,-3,3,2,null,11,3,-2,null,1]"), 8))