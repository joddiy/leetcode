import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        array = [(root, 0)]
        ret = []
        cur_level = -1
        cur_sum = 0.
        cur_num = 0.
        while array:
            node, level = array.pop(0)
            if cur_level != level:
                if cur_num > 0:
                    ret.append(cur_sum / cur_num)
                cur_sum = float(node.val)
                cur_num = 1.
                cur_level = level
            else:
                cur_sum += float(node.val)
                cur_num += 1.
            if node.left:
                array.append((node.left, level + 1))
            if node.right:
                array.append((node.right, level + 1))
        if cur_num > 0:
            ret.append(cur_sum / cur_num)
        return ret


solution = Solution().countNodes
print(solution(stringToTreeNode("[3,9,20,15,7]")))
