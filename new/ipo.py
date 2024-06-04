import math
import pprint
import sys

from tools import *
from collections import defaultdict

from heapq import *


class Solution(object):
    @print_
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        if w >= max(capital):
            return w + sum(nlargest(k, profits))
        projects = [[capital[i], profits[i]] for i in range(len(profits))]
        projects.sort(key=lambda x: x[0])
        heap = []
        for i in range(k):
            while projects and projects[0][0] <= w:
                heappush(heap, -1 * projects.pop(0)[1])
            if not heap:
                break
            p = -heappop(heap)
            w += p
        return w


solution = Solution().findMaximizedCapital
solution(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1])
solution(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2])
