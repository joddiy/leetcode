import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # recursively
        # def is_same(root1, root2):
        #     if root1 is None and root2 is None:
        #         return True
        #     elif root1 is not None and root2 is not None:
        #         if root1.val != root2.val:
        #             return False
        #         else:
        #             return is_same(root1.left, root2.right) and is_same(root1.right, root2.left)
        #     else:
        #         return False
        #
        # return is_same(root, root)
        # iteratively
        list1 = [root]
        list2 = [root]
        while list1 and list2:
            node1 = list1.pop(0)
            node2 = list2.pop(0)
            if node1 is None and node2 is None:
                continue
            elif node1 is not None and node2 is not None:
                if node1.val != node2.val:
                    return False
                else:
                    list1.extend([node1.left, node1.right])
                    list2.extend([node2.right, node2.left])
            else:
                return False

        return len(list1) == len(list2)


solution = Solution().isSymmetric
print(solution(stringToTreeNode("[1,2,2,3,4,4,3]")))
