import sys

from tools import *
import pprint


class Solution(object):

    @print_
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, key=lambda x: -x)
        h = 0
        while h < len(citations) and h + 1 <= citations[h]:
            h += 1
        return h


solution = Solution().hIndex
solution(citations=[3, 0, 6, 1, 5])
solution(citations=[1, 3, 1])
