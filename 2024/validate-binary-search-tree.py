import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root]
        while stack[-1].left:
            stack.append(stack[-1].left)
        pre_v = None
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                while stack[-1].left:
                    stack.append(stack[-1].left)
            if pre_v is not None and node.val <= pre_v:
                return False
            pre_v = node.val
        return True


solution = Solution().isValidBST
solution(root=stringToTreeNode("[2,1,3]"))
solution(root=stringToTreeNode("[5,1,4,null,null,3,6]"))
solution(root=stringToTreeNode("[2,2,2]"))
