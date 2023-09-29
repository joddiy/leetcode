import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map_ = {}
        for i, n in enumerate(nums):
            if n in map_ and i - map_[n] <= k:
                return True
            else:
                map_[n] = i
        return False


solution = Solution().containsNearbyDuplicate
solution(nums=[1, 2, 3, 1], k=3)
solution(nums=[1, 2, 3, 1, 2, 3], k=2)
solution(nums=[1, 0, 1, 1], k=1)
