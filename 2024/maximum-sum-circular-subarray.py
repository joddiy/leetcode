import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


solution = Solution().maxSubarraySumCircular
solution(nums=[1, -2, 3, -2])
solution(nums=[5, -3, 5])
solution(nums=[-3, -2, -3])
