import math
import sys

from tools import *
import pprint
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    @print_
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        array = [(root, 0)]
        cur_level = 0
        pre_node = None
        while array:
            node, level = array.pop(0)
            if pre_node is not None and level == cur_level:
                pre_node.next = node
            pre_node = node
            cur_level = level
            if node.left:
                array.append((node.left, level + 1))
            if node.right:
                array.append((node.right, level + 1))
        return root


solution = Solution().connect
solution(root=stringToTreeNode("[1,2,3,4,5,null,7]"))
solution(root=stringToTreeNode("[]"))
