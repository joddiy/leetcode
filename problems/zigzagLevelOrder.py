from tools import *


class Solution(object):
    @print_
    @tree_node
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []

        def recursive(root, i):
            if not root:
                return
            if i >= len(ret):
                ret.append([])
            if i % 2 == 0:
                ret[i].append(root.val)
            else:
                ret[i].insert(0, root.val)
               
            recursive(root.left, i + 1)
            recursive(root.right, i + 1)


        recursive(root, 0)
        return ret


solution = Solution().zigzagLevelOrder

solution("[3,9,20,null,null,15,7]")