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
        if not root:
            return 0

        array = [root]
        i = 0
        while array:
            node = array.pop(0)
            if node.left:
                array.append(node.left)
            if node.right:
                array.append(node.right)
            i += 1
        return i


solution = Solution().countNodes
print(solution(stringToTreeNode("[1,2,3,4,5,6]")))
print(solution(stringToTreeNode("[1,2,3,4,5,6,7]")))
print(solution(stringToTreeNode("[1,2,3,4,5,6,7]")))
