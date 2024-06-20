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
        i = 0
        while i < len(citations):
            if citations[i] >= (i+1):
                pass
            else:
                break
            i += 1
        return i


solution = Solution().hIndex
solution(citations=[3, 0, 6, 1, 5])
solution(citations=[1, 3, 1])
