import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sum_below(cur_base, root):
            if not root:
                return 0

            cur_base = cur_base * 10 + root.val
            if not root.left and not root.right:
                return cur_base
            elif root.left and root.right:
                return sum_below(cur_base, root.left) + sum_below(cur_base, root.right)
            elif root.left:
                return sum_below(cur_base, root.left)
            else:
                return sum_below(cur_base, root.right)

        return sum_below(0, root)


solution = Solution().sumNumbers
print(solution(stringToTreeNode("[1,2,3]")))
print(solution(stringToTreeNode("[4,9,0,5,1]")))
print(solution(stringToTreeNode("[4,9,0,null,1]")))
print(solution(stringToTreeNode("[]")))
