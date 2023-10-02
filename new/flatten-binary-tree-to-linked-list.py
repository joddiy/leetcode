import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def recursive(root):
            if not root.left and not root.right:
                return root, root
            elif root.left and root.right:
                left_head, left_tail = recursive(root.left)
                right_head, right_tail = recursive(root.right)
                root.right = left_head
                root.left = None
                left_tail.right = right_head
                return root, right_tail
            elif root.left:
                left_head, left_tail = recursive(root.left)
                root.right = left_head
                root.left = None
                return root, left_tail
            else:
                right_head, right_tail = recursive(root.right)
                return root, right_tail

        if root:
            recursive(root)
        return root


solution = Solution().flatten
print(treeNodeToString(solution(stringToTreeNode("[1,2,5,3,4,null,6]"))))
