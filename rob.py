from utils.tools import stringToTreeNode, treeNodeToString, TreeNode


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #1: rob, 2: not rob
        def recursive(root):
            if not root:
                return (0, 0)
            L_maxes = recursive(root.left)
            R_maxes = recursive(root.right)
            return (
                L_maxes[1] + R_maxes[1] + root.val,
                max(L_maxes) + max(R_maxes)
            )

        return max(recursive(root))


Solution().rob(stringToTreeNode("[3,2,3,null,3,null,1]"))
