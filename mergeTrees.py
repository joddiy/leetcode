from utils.tools import *


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val  # save some space
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def traverse(t1, t2):  # avoid some unnecessary merge
            t1.val += t2.val
            if t2.left:
                if not t1.left:
                    t1.left = TreeNode(0)
                traverse(t1.left, t2.left)
            if t2.right:
                if not t1.right:
                    t1.right = TreeNode(0)
                traverse(t1.right, t2.right)
            return

        if t1 and t2:
            traverse(t1, t2)
            return t1
        else:
            return t1 if t1 else t2


print(treeNodeToString(Solution().mergeTrees(stringToTreeNode(
    "[1,3,2,5]"), stringToTreeNode("[2,1,3,null,4,7]"))))
