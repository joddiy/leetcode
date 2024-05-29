import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        array = [(root, 0)]
        ret = []
        while array:
            node, level = array.pop(0)
            if node.left:
                array.append((node.left, level + 1))
            if node.right:
                array.append((node.right, level + 1))
            if not array or level != array[0][1]:
                ret.append(node.val)
        return ret


solution = Solution().rightSideView
solution(root=stringToTreeNode("[1,2,3,null,5,null,4]"))
solution(root=stringToTreeNode("[1,null,3]"))
solution(root=stringToTreeNode("[]"))
