from utils.tools import *


class Solution(object):
    # dfs
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # bfs
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == []) | (root is None):
            return 0
        q, cnt = [root], 0
        while q:
            cnt += 1
            # each layer's list from left to right
            q = [y for x in q for y in [x.left, x.right] if y is not None]
        return cnt


print(Solution().maxDepth(stringToTreeNode("[3,9,20,null,null,15,7]")))
