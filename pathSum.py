from utils.tools import *


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def recursive(root, res):
            if root:
                res.append(root.val)
                recursive(root.left, res)
                recursive(root.right, res)

        res = []
        recursive(root, res)
        return res


Solution().pathSum(stringToTreeNode("[10,5,-3,3,2,null,11,3,-2,null,1]"), 8)
