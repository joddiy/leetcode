# -*- coding: utf-8 -*-
# file: isSymmetric.py
# author: joddiyzhang@gmail.com
# time: 2018/11/21 2:44 PM
# ------------------------------------------------------------------------

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        queue2 = [root]
        while queue and queue2:
            node = queue.pop(0)
            node2 = queue2.pop(0)
            if node and node2:
                if node.val != node2.val:
                    return False
                queue.append(node.right)
                queue.append(node.left)
                queue2.append(node2.left)
                queue2.append(node2.right)
            elif node is None and node2 is None:
                continue
            else:
                return False
        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isMirror(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t1 is None:
                return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

        return isMirror(root, root)
