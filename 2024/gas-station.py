import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        i, j = 0, 0
        cur = gas[i] - cost[i]
        while j - i < n - 1:
            if cur < 0:
                i -= 1
                cur += gas[i] - cost[i]
            else:
                j += 1
                cur += gas[j] - cost[j]
        if cur < 0:
            return -1
        else:
            return i % n


solution = Solution().canCompleteCircuit
solution(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
solution(gas=[2, 3, 4], cost=[3, 4, 3])
