# -*- coding: utf-8 -*-
# file: invertTree.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 6:16 PM
# ------------------------------------------------------------------------

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        new_root = TreeNode(root.val)
        tmp_list = [root] # BFS
        tmp_list2 = [new_root]
        while len(tmp_list) != 0:
            cur_node = tmp_list.pop(0)
            cur_node2 = tmp_list2.pop(0)
            cur_node2.val = cur_node.val
            if cur_node.right is not None:
                tmp_list.append(cur_node.right)
                cur_node2.left = TreeNode(cur_node.right.val)
                tmp_list2.append(cur_node2.left)
            if cur_node.left is not None:
                tmp_list.append(cur_node.left)
                cur_node2.right = TreeNode(cur_node.left.val)
                tmp_list2.append(cur_node2.right)
        return new_root

    # BFS
    def invertTree(self, root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                # first insert into the queue
                queue.append(node.right)
                queue.append(node.left)
                # then switch its local children
                node.left, node.right = node.right, node.left
        return root

    # DFS
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                # first reach the deepest node
                stack.extend([node.left, node.right])  # can change to [node.right, node.left]
                # then switch its local children
                node.left, node.right = node.right, node.left
        return root

    # recursively
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
