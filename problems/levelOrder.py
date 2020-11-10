from tools import *


class Solution(object):
    @print_
    @tree_node
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []

        def recursive(root, i):
            if not root:
                return
            if i >= len(ret):
                ret.append([])
            ret[i].append(root.val)
            recursive(root.left, i + 1)
            recursive(root.right, i + 1)

        recursive(root, 0)
        return ret

    @print_
    @tree_node
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []

        queue = [(0, root)]
        while queue:
            level, node = queue.pop(0)
            if not node:
                continue
            if level > len(ret) - 1:
                ret.append([])
            ret[level].append(node.val)
            queue.extend([(level + 1, node.left), (level + 1, node.right)])
        return ret

solution = Solution().levelOrder

solution("[3,9,20,null,null,15,7]")