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
        cur = gas[0] - cost[0]
        n = len(gas)
        l, r = 0, 0
        i = 1
        while i < n:
            if cur < 0:
                l -= 1
                cur += (gas[l] - cost[l])
            else:
                r += 1
                cur += (gas[r] - cost[r])
            i += 1
        if cur >= 0:
            return l % n
        else:
            return -1


solution = Solution().canCompleteCircuit
solution(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
solution(gas=[2, 3, 4], cost=[3, 4, 3])
