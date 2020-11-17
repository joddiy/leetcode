from tools import *


class Solution(object):
    @print_
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        def recusive(remaining, prefix):
            if not remaining:
                ret.append(prefix)
            else:
                for i in range(len(remaining)):
                    recusive(remaining[0:i] + remaining[i + 1:],
                             prefix + [remaining[i]])

        recusive(nums, [])
        return ret


solution = Solution().permute

solution([1, 2, 3])
solution([])
