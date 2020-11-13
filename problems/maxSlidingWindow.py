from tools import *


class Solution(object):
    @print_
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_ = max(nums[0:k])
        ret = [max_]
        for i in range(k, len(nums)):
            if nums[i] >= max_:
                max_ = nums[i]
            elif nums[i - k] != max_:
                pass
            else:
                max_ = max(nums[i + 1 - k:i + 1])
            ret.append(max_)
        return ret


solution = Solution().maxSlidingWindow

solution(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
solution(nums=[1], k=1)
solution(nums=[1, -1], k=1)
solution(nums=[9, 11], k=2)
solution(nums=[4, -2], k=2)