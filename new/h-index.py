import pprint

from tools import *


class Solution(object):
    @print_
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse=True)
        citations.append(0)
        for i, c in enumerate(citations):
            if i + 1 > c:
                return i


solution = Solution().hIndex
solution([3, 0, 6, 1, 5])
solution([1, 3, 1])
solution([3])
solution([0])
solution([11, 15])
