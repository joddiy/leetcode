from utils.tools import *


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # pre-order dfs
        def traverse(node, level):
            if node:
                if len(res) <= level:
                    res.append([])
                res[level].append(node.val)
                traverse(node.left, level + 1)
                traverse(node.right, level + 1)

        res = []
        traverse(root, 0)
        return res

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [(root, 0)]
        output = []
        while queue:
            node, level = queue.pop(0)
            if node:
                if len(output) <= level:
                    output.append([])
                output[level].append(node.val)
                queue.extend([(node.left, level + 1), (node.right, level + 1)])
        return output


print(Solution().levelOrder(stringToTreeNode("[3,9,20,null,null,15,7]")))
