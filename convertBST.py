# -*- coding: utf-8 -*-
# file: convertBST.py
# author: joddiyzhang@gmail.com
# time: 2018/11/21 12:05 PM
# ------------------------------------------------------------------------

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        def sumBST(root, upper):
            if root.right is not None:
                upper = sumBST(root.right, upper)
            root.val += upper
            upper = root.val
            if root.left:
                upper = sumBST(root.left, upper)
            return upper

        sumBST(root, 0)
        return root

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        prev = 0
        self.inorder(root, prev)
        return root

    def inorder(self, root, prev):
        if not root:
            return prev
        else:
            root.val += self.inorder(root.right, prev)  # right value needs to add the previous upper
            return self.inorder(root.left, root.val)  # left value needs to add its root value

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        stack = [root]
        node = root.right
        sumVal = 0

        while stack or node:
            while node:  # first add all reach the deepest right nodes
                stack.append(node)
                node = node.right

            node = stack.pop()  # no more right node
            sumVal += node.val  # sum of all add current node
            node.val = sumVal  # replace current value with all sum

            node = node.left  # talk about its left node

        return root
