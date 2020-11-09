from tools import *


class Solution(object):
    @print_
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights + [0]
        n = len(heights)
        l_dp, r_dp = [0] * n, [0] * n
        for i in range(1, n - 1):
            j = i - 1
            while j > 0 and heights[j] >= heights[i]:
                j = l_dp[j]
            l_dp[i] = j

        for i in range(n - 2, 0, -1):
            j = i + 1
            while j > 0 and heights[j] >= heights[i]:
                j = r_dp[j]
            r_dp[i] = j

        ret = 0
        for i in range(1, n - 1):
            ret = max(ret, (r_dp[i] - l_dp[i] - 1) * heights[i])
        return ret


solution = Solution().largestRectangleArea

solution([2, 1, 5, 6, 2, 3])
solution([0])
solution([])