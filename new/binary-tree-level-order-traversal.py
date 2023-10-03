import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        array = [(root, 0)]
        ret = []
        cur_level = -1
        cur_ret = []
        while array:
            node, level = array.pop(0)
            if cur_level != level:
                if cur_ret:
                    ret.append(cur_ret)
                cur_ret = [node.val]
                cur_level = level
            else:
                cur_ret.append(node.val)
            if node.left:
                array.append((node.left, level + 1))
            if node.right:
                array.append((node.right, level + 1))
        if cur_ret:
            ret.append(cur_ret)
        return ret


solution = Solution().levelOrder
print(solution(stringToTreeNode("[3,9,20,null,null,15,7]")))
