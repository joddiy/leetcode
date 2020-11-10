from tools import *


class Solution(object):
    @print_
    @tree_node
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        map_ = {i: idx for idx, i in enumerate(inorder)}

        def build(i, j):
            if i > j:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            m = map_[val]
            root.left = build(i, m - 1)
            root.right = build(m + 1, j)
            return root

        return build(0, len(preorder) - 1)


solution = Solution().buildTree

solution([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
