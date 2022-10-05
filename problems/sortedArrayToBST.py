from tools import *


class Solution(object):
    @print_
    @tree_node
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        n = len(nums)

        def create(i, j):
            if i > j:
                return None
            m = (i + j) // 2
            root = TreeNode(nums[m])
            root.left = create(i, m - 1)
            root.right = create(m + 1, j)
            return root

        return create(0, n - 1)


solution = Solution().sortedArrayToBST

solution([-10, -3, 0, 5, 9])
