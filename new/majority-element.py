import pprint

from tools import *


class Solution(object):
    @print_
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj, cnt = None, 0
        for num in nums:
            if cnt == 0:
                maj = num
                cnt = 1
            elif num == maj:
                cnt += 1
            else:
                cnt -= 1
        return maj


solution = Solution().majorityElement

solution([3, 2, 3])
solution([2, 2, 1, 1, 1, 2, 2])
