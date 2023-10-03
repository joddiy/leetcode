import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_diff = sys.maxsize

        def get_min_max(root):
            l_min, r_max = root.val, root.val
            if root.left:
                l_min, l_max = get_min_max(root.left)
                self.min_diff = min(root.val - l_max, self.min_diff)
            if root.right:
                r_min, r_max = get_min_max(root.right)
                self.min_diff = min(r_min - root.val, self.min_diff)
            return l_min, r_max

        get_min_max(root)
        return self.min_diff


solution = Solution().getMinimumDifference
print(solution(stringToTreeNode("[4,2,6,1,3]")))
print(solution(stringToTreeNode("[1,0,48,null,null,12,49]")))
