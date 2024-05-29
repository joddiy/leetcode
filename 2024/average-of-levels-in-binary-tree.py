import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        array = [(root, 0)]
        ret = []
        sum_ = 0
        cnt_ = 0
        while array:
            node, level = array.pop(0)
            if node.left:
                array.append((node.left, level + 1))
            if node.right:
                array.append((node.right, level + 1))
            sum_ += float(node.val)
            cnt_ += 1.
            if not array or level != array[0][1]:
                ret.append(sum_ / cnt_)
                sum_ = 0
                cnt_ = 0
        return ret


solution = Solution().averageOfLevels
solution(root=stringToTreeNode("[3,9,20,null,null,15,7]"))
solution(root=stringToTreeNode("[3,9,20,15,7]"))
