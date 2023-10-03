import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.is_valid = True

        def get_min_max(root):
            l_min, r_max = root.val, root.val
            if root.left:
                l_min, l_max = get_min_max(root.left)
                if l_max >= root.val:
                    self.is_valid = False
            if root.right:
                r_min, r_max = get_min_max(root.right)
                if r_min <= root.val:
                    self.is_valid = False
            return l_min, r_max

        get_min_max(root)
        return self.is_valid


solution = Solution().isValidBST
print(solution(stringToTreeNode("[2,1,3]")))
print(solution(stringToTreeNode("[5,1,4,null,null,3,6]")))
