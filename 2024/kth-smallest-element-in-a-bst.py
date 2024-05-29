import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [root]
        while stack[-1].left:
            stack.append(stack[-1].left)
        i = 0
        node = None
        while i < k:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                while stack[-1].left:
                    stack.append(stack[-1].left)
            i += 1
        return node.val


solution = Solution().kthSmallest
solution(root=stringToTreeNode("[3,1,4,null,2]"), k=1)
solution(root=stringToTreeNode("[5,3,6,2,4,null,null,1]"), k=3)
