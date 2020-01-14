from utils.tools import *


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root

        def recursive(root):
            if root.left is None and root.right is None:
                return root
            if root.left:
                deepest = recursive(root.left)
                tmp = root.right
                root.right = root.left
                root.left = None
                deepest.right = tmp
            if root.right:
                return recursive(root.right) # the deepest node for upper left node

        recursive(root)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        n = root
        while n:
            if n.left:
                last = n.left
                while last.right:
                    last = last.right
                last.right = n.right
                n.right = n.left
                n.left = None
            n = n.right

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root

        stack = []
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        root.left = None
        head = root
        current = root
        while stack:
            node = stack.pop()
            print(stack)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            node.left = None
            current.right = node
            current = node


root = stringToTreeNode("[1,2,5,3,4,6]")
Solution().flatten(root)
print(treeNodeToString(root))
