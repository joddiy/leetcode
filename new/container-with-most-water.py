from tools import *
import pprint


class Solution(object):
    @print_
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # area: min(height[l], height[r])*(r-l)
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


solution = Solution().maxArea
solution([1, 8, 6, 2, 5, 4, 8, 3, 7])
