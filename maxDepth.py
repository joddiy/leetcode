# -*- coding: utf-8 -*-
# file: maxDepth.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 7:06 PM
# ------------------------------------------------------------------------

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

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
            q = [y for x in q for y in [x.left, x.right] if y is not None]  ## each layer's list from left to right
        return cnt
