# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        output = []
        tmp = []
        cur_cnt = 1
        next_cnt = 0
        while queue:
            node = queue.pop(0)
            if node:
                cur_cnt -= 1
                tmp.append(node.val)
                if node.left:
                    next_cnt += 1
                if node.right:
                    next_cnt += 1
                if cur_cnt == 0:
                    cur_cnt = next_cnt
                    next_cnt = 0
                    output.append(tmp)
                    tmp = []
                queue.extend([node.left, node.right])
        return output

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

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