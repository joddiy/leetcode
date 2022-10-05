from tools import *


class Solution(object):
    @print_
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The main idea is based on greedy.
        # Let's say the range of the current jump is [curBegin, curEnd],
        # curFarthest is the farthest point that all points in [curBegin, curEnd] can reach.
        # Once the current point reaches curEnd, then trigger another jump,
        # and set the new curEnd with curFarthest, then keep the above steps
        result = 0
        global_right = 0
        local_right = 0

        for i, num in enumerate(nums):
            if i > local_right:
                local_right = global_right
                result += 1
            global_right = max(global_right, i + num)
        return result


solution = Solution().jump

solution([2, 3, 1, 1, 4])
solution([2, 3, 0, 1, 4])
solution([2, 1])
