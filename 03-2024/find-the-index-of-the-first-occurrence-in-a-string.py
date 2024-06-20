import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        k = len(needle)
        for i in range(n - k + 1):
            if haystack[i:i + k] == needle:
                return i
        return -1


solution = Solution().strStr
solution(haystack="sadbutsad", needle="sad")
solution(haystack="leetcode", needle="leeto")
