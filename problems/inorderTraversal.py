from tools import *


class Solution(object):
    @print_
    @tree_node
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ret.append(root.val)
            inorder(root.right)

        inorder(root)
        return ret

    @print_
    @tree_node
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        queue = [root]

        while queue:
            node = queue.pop(-1)
            if not node:
                continue
            elif isinstance(node, TreeNode):
                queue.extend([node.right, node.val, node.left])
            else:
                ret.append(node)

        return ret


solution = Solution().inorderTraversal

solution("[1,null,2,3]")
