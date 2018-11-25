from utils.tools import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        found_set = set()
        stack = [(root, False)]
        while stack:
            node, label = stack.pop()
            if node:
                if label:
                    if node.val == p.val or node.val == q.val:
                        found_set.add(node)
                        if node.left and node.left in found_set:
                            return node
                        if node.right and node.right in found_set:
                            return node
                    elif node.left and node.left in found_set:
                        found_set.add(node)
                    elif node.right and node.right in found_set:
                        found_set.add(node)
                    if node.left and node.right and node.left in found_set and node.right in found_set:
                        return node
                else:
                    stack.extend([(node, True), (node.right, False), (node.left, False)])
        return None
