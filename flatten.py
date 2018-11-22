# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
                return recursive(root.right)

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