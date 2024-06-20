import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        array = [(root, 0)]
        ret = []
        cur_level = -1
        cur_val = None
        while array:
            node, level = array.pop(0)
            if cur_level != level:
                if cur_val is not None:
                    ret.append(cur_val)
                cur_val = node.val
                cur_level = level
            else:
                cur_val = node.val
            if node.left:
                array.append((node.left, level + 1))
            if node.right:
                array.append((node.right, level + 1))
        if not ret or cur_val != ret[-1]:
            ret.append(cur_val)
        return ret


solution = Solution().rightSideView
print(solution(stringToTreeNode("[1,2,3,null,5,6,null,4]")))
print(solution(stringToTreeNode("[1]")))
