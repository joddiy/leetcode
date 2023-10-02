import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p:
        :type q:
        :rtype: TreeNode
        """
        self.lca = None

        def recursive(root):
            if not root:
                return 0
            ret = recursive(root.left) + recursive(root.right)
            if root is p or root is q:
                ret += 1
            if ret == 2 and self.lca is None:
                self.lca = root
            return ret

        recursive(root)
        return self.lca


solution = Solution().lowestCommonAncestor
print(solution(stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"), p=5, q=1))
