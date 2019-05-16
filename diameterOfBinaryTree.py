from utils.tools import stringToTreeNode, treeNodeToString, TreeNode


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1

        def recursive(root):
            if root:
                recursive(root.left)
                recursive(root.right)
                a, b = 0, 0
                if root.left:
                    a = root.left.val
                if root.right:
                    b = root.right.val
                root.val = max(a, b) + 1
                self.ans = max(
                    self.ans, a + b)

        recursive(root)
        return self.ans

    def diameterOfBinaryTree(self, root):
        self.ans = 1

        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


Solution().diameterOfBinaryTree(stringToTreeNode("[1,2,3,4,5,null,null]"))
