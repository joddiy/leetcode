from utils.tools import *


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
                    stack.extend(
                        [(node, True), (node.right, False), (node.left, False)])
        return None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.low_desc = None

        def re(root, p, q):
            if not root:
                return False
            left_res = re(root.left, p, q)
            right_res = re(root.right, p, q)
            if root.val == p or root.val == q:
                if left_res or right_res:
                    self.low_desc = root
                    return False
                else:
                    return True
            elif left_res and right_res:
                self.low_desc = root
                return False
            else:
                return left_res or right_res
        re(root, p.val, q.val)
        return self.low_desc


# print(Solution().lowestCommonAncestor(
#     stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"), TreeNode(5), TreeNode(1)))
print(Solution().lowestCommonAncestor(
    stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"), TreeNode(5), TreeNode(4)).val)
