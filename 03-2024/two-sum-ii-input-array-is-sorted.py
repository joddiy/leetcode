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
        i, j = 0, len(numbers) - 1
        while i < j:
            val = numbers[i] + numbers[j]
            if val < target:
                i += 1
            elif val > target:
                j -= 1
            else:
                return [i + 1, j + 1]


solution = Solution().twoSum
solution(numbers=[2, 7, 11, 15], target=9)
solution(numbers=[2, 3, 4], target=6)
