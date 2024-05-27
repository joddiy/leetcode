import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        ret = 0
        while i != j:
            ret = max(ret, min(height[i], height[j]) * (j - i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return ret


solution = Solution().maxArea
solution(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
