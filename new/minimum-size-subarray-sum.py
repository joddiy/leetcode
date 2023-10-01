from tools import *
import pprint


class Solution(object):
    @print_
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """


solution = Solution().minSubArrayLen
solution(target=7, nums=[2, 3, 1, 2, 4, 3])
solution(target=4, nums=[1, 4, 4])
solution(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1])
solution(target=213, nums=[12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12])
