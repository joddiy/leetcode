import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        array = [(root, 0)]
        ret = [[]]
        while array:
            node, level = array.pop(0)
            if node.left:
                array.append((node.left, level + 1))
            if node.right:
                array.append((node.right, level + 1))
            if level % 2 == 1:
                ret[-1].insert(0, node.val)
            else:
                ret[-1].append(node.val)
            if array and level != array[0][1]:
                ret.append([])
        return ret

solution = Solution().zigzagLevelOrder
solution(root=stringToTreeNode("[3,9,20,null,null,15,7]"))
solution(root=stringToTreeNode("[1]"))
solution(root=stringToTreeNode("[]"))
