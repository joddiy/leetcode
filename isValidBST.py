from utils.tools import TreeNode, stringToTreeNode


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recursive(root, max_v, min_v):
            left, right = True, True
            if root.left:
                t_max_v = min(root.val, max_v) if max_v else root.val
                if t_max_v is not None and root.left.val >= t_max_v:
                    return False
                elif min_v is not None and root.left.val <= min_v:
                    return False
                else:
                    left = recursive(root.left, t_max_v, min_v)
            if root.right:
                t_min_v = max(root.val, min_v) if min_v else root.val
                if t_min_v is not None and root.right.val <= t_min_v:
                    return False
                elif max_v is not None and root.right.val >= max_v:
                    return False
                else:
                    right = recursive(root.right, max_v, t_min_v)
            return left and right

        if not root:
            return True
        else:
            return recursive(root, None, None)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._dfs(root, float("-inf"), float("inf"))

    def _dfs(self, node, left_val, right_val):
        if not node:
            return True

        if node.val <= left_val:
            return False

        if node.val >= right_val:
            return False

        return self._dfs(node.left, left_val, node.val) and self._dfs(node.right, node.val, right_val)


# print(Solution().isValidBST(stringToTreeNode('[5,1,4,null,null,3,6]')))
# print(Solution().isValidBST(stringToTreeNode('[10,5,15,null,null,6,20]')))
# print(Solution().isValidBST(stringToTreeNode('[2,1,3]')))
print(Solution().isValidBST(stringToTreeNode('[0,null,-1]')))
