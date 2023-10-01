import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if p.val != q.val:
                return False
            elif self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
        else:
            return False


solution = Solution().isSameTree
print(solution(p=stringToTreeNode("[1,2,3]"), q=stringToTreeNode("[1,2,3]")))
print(solution(p=stringToTreeNode("[1,2]"), q=stringToTreeNode("[1,null,2]")))
print(solution(p=stringToTreeNode("[1,2,1]"), q=stringToTreeNode("[1,1,2]")))
