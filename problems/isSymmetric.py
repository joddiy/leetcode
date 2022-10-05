from tools import *


class Solution(object):
    @print_
    @tree_node
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def recursive(l, r):
            if not l and not r:
                return True
            elif l and r:
                return l.val == r.val and recursive(
                    l.left, r.right) and recursive(l.right, r.left)
            else:
                return False

        return recursive(root.left, root.right)

    @print_
    @tree_node
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue1 = [root.left, root.right]
        queue2 = [root.right, root.left]

        while queue1 and queue2:
            node1 = queue1.pop(0)
            node2 = queue2.pop(0)
            if not node1 and not node2:
                continue
            elif node1 and node2 and node1.val == node2.val:
                queue1.extend([node1.left, node1.right])
                queue2.extend([node2.right, node2.left])
            else:
                return False
        if not queue1 and not queue2:
            return True
        else:
            return False


solution = Solution().isSymmetric

solution("[1,2,2,3,4,4,3]")
solution("[1,2,3]")