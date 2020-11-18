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
        map_ = {v: i for i, v in enumerate(inorder)}

        def build(i, j):
            if i > j:
                return None
            v = inorder.pop(0)
            root = TreeNode(v)
            root.left = build(i, map_[v] - 1)
            root.right = build(map_[v] + 1, j)
            return root

        return build(0, len(preorder) - 1)


solution = Solution().buildTree

solution([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
