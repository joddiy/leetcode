import pprint
from tools import *


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """



solution = Solution().canCompleteCircuit
solution(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
solution(gas=[2, 3, 4], cost=[3, 4, 3])
