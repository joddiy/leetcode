from tools import *


class Solution(object):
    @print_
    @tree_node
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def merge(t1, t2):
            if not t1 and not t2:
                return None
            elif not t1:
                return t2
            elif not t2:
                return t1
            else:
                t1.left = merge(t1.left, t2.left)
                t1.right = merge(t1.right, t2.right)
                t1.val = t1.val + t2.val
                return t1

        return merge(t1, t2)


solution = Solution().mergeTrees

solution("[1,3,2,5]", "[2,1,3,null,4,null,7]")
