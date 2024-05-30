import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def build(i, j):
            if i > j:
                return None
            m = (i + j) // 2
            node = TreeNode(nums[m])
            node.left = build(i, m - 1)
            node.right = build(m + 1, j)
            return node

        return build(0, len(nums) - 1)


solution = Solution().sortedArrayToBST
solution(nums=[-10, -3, 0, 5, 9])
