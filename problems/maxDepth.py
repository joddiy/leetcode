from tools import *


class Solution(object):
    @print_
    @tree_node
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(root):
            if not root:
                return 0
            return max(find(root.left), find(root.right)) + 1

        return find(root)

    @print_
    @tree_node
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0

        queue = [(0, root)]
        while queue:
            level, node = queue.pop(0)
            if not node:
                continue
            ret = max(ret, level + 1)
            queue.extend([(level + 1, node.left), (level + 1, node.right)])
        return ret


solution = Solution().maxDepth

solution("[3,9,20,null,null,15,7]")