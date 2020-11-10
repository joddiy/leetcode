from tools import *
import sys


class Solution(object):
    @print_
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas:
            return -1
        n = len(gas)
        sum_ = 0
        min_sum = sys.maxsize
        ret = 0
        for i in range(n):
            sum_ += (gas[i] - cost[i])
            if sum_ < min_sum:
                min_sum = sum_
                ret = i
        return -1 if sum_ < 0 else (ret + 1) % n


solution = Solution().canCompleteCircuit

# solution([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
solution([4, 5, 1, 2, 3], [1, 2, 3, 4, 5])
# solution([2, 3, 4], [3, 4, 3])
