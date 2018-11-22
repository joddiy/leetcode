# -*- coding: utf-8 -*-
# file: inorderTraversal.py
# author: joddiyzhang@gmail.com
# time: 2018/11/22 9:59 PM
# ------------------------------------------------------------------------

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        p = root
        stack = []
        output = []
        while p or stack:
            while p:
                stack.append(p)
                p = p.left  # first, go to the deepest left
            if stack:
                p = stack.pop()
                output.append(p.val)  # output the top of stack
                p = p.right  # take one right node
                # when right is None, will pop a new node at next iteration
        return output
