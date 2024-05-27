import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## 1
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        ## 2
        # map_ = {v: k for k, v in enumerate(numbers)}
        # for i in range(len(numbers)):
        #     j = target - numbers[i]
        #     if j in map_:
        #         return [i + 1, map_[j] + 1]
        ## 3
        i, j = 0, len(numbers) - 1
        while i < len(numbers) and j >= 0:
            sum_ = numbers[i] + numbers[j]
            if sum_ < target:
                i += 1
            elif sum_ > target:
                j -= 1
            else:
                return i + 1, j + 1


solution = Solution().twoSum
solution(numbers=[2, 7, 11, 15], target=9)
solution(numbers=[2, 3, 4], target=6)
