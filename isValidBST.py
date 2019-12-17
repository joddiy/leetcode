from utils.tools import TreeNode, stringToTreeNode


class Solution(object):
    # compare from down to up, which must larger than max value of left subtree
    # and less than min value of right subtree
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

    # compare from up to down, we set a range by low bound and upper bound,
    # each time we enter a left tree, we constrict the upper bound,
    # and when we enter the right tree, we constrict the right bound
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _dfs(node, lower_bound, upper_bound):
            if not node:
                return True
            if node.val <= lower_bound:
                return False
            if node.val >= upper_bound:
                return False
            return _dfs(node.left, lower_bound, node.val) and _dfs(node.right, node.val, upper_bound)

        return self._dfs(root, float("-inf"), float("inf"))


# print(Solution().isValidBST(stringToTreeNode('[5,1,4,null,null,3,6]')))
# print(Solution().isValidBST(stringToTreeNode('[10,5,15,null,null,6,20]')))
# print(Solution().isValidBST(stringToTreeNode('[2,1,3]')))
print(Solution().isValidBST(stringToTreeNode('[0,null,-1]')))
