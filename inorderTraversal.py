from utils.tools import TreeNode, stringToTreeNode, treeNodeToString


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        p = root
        stack = []
        output = []
        while p or stack:
            while p:
                stack.append(p)
                p = p.left  # first, go to the deepest left
            if stack:
                p = stack.pop()
                output.append(p.val)  # output the top of stack
                p = p.right  # take one right node
                # when right is None, will pop a new node at next iteration
        return output


print(Solution().inorderTraversal(stringToTreeNode("[1,null,2,3]")))
