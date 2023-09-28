import pprint
from tools import *


class Solution(object):
    @print_
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        i, j, cur_gas = 0, 0, gas[0] - cost[0]
        while j - i + 1 < n:
            if cur_gas < 0:
                i -= 1
                cur_gas += gas[i] - cost[i]
            else:
                j += 1
                cur_gas += gas[j] - cost[j]
        if cur_gas < 0:
            return -1
        else:
            return i % n


solution = Solution().canCompleteCircuit
# solution(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
solution(gas=[2, 3, 4], cost=[3, 4, 3])
