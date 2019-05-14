from utils.tools import stringToTreeNode, treeNodeToString

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        print(treeNodeToString(root))
        return 0


Solution().rob(stringToTreeNode("[3,2,3,null,3,null,1]"))
