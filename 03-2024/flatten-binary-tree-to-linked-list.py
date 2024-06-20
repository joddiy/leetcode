import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node:
                return None, None
            else:
                l_head, l_tail = dfs(node.left)
                r_head, r_tail = dfs(node.right)
                node.left = None
                t = node
                if l_head:
                    t.right = l_head
                    t = l_tail
                if r_head:
                    t.right = r_head
                    t = r_tail
                return node, t

        head, tail = dfs(root)
        return head


solution = Solution().flatten
solution(root=stringToTreeNode("[1,2,5,3,4,null,6]"))
solution(root=stringToTreeNode("[]"))
solution(root=stringToTreeNode("[1,2]"))
