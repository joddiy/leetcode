from tools import *


class Solution(object):
    @print_
    @tree_node
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if not root:
                return None
            left_tail = helper(root.left)
            right_tail = helper(root.right)
            if not left_tail and not right_tail:
                return root
            elif left_tail and right_tail:
                root.right, left_tail.right = root.left, root.right
                root.left = None
                return right_tail
            elif left_tail:
                root.right, left_tail.right = root.left, root.right
                root.left = None
                return left_tail
            else:
                return right_tail

        helper(root)
        return root

    @print_
    @tree_node
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        # return the deepest node which has been flatten
        def dfs(root):
            if not root.left and not root.right:
                return root
            deepest = None
            if root.left:
                deepest = dfs(root.left)
                deepest.right = root.right
                root.right = root.left
                root.left = None
            if root.right:
                return dfs(deepest) if deepest else dfs(root.right)

        dfs(root)
        return root

    @print_
    @tree_node
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        stack = [root]
        ret = TreeNode(None)
        head = ret
        while stack:
            node = stack.pop(-1)
            if not node:
                continue
            else:
                stack.extend([node.right, node.left])
                node.left, node.right = None, None
                head.right = node
                head = head.right
        return ret.right


solution = Solution().flatten

solution("[1,2,5,3,4,6]")