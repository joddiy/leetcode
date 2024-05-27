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
        l, i = 0, 0
        while l < len(haystack) - len(needle) + 1:
            while i < len(needle):
                if haystack[l + i] == needle[i]:
                    i += 1
                else:
                    i = 0
                    break
            if i == len(needle):
                return l
            l += 1
        return -1


solution = Solution().strStr
solution(haystack="sadbutsad", needle="sad")
solution(haystack="leetcode", needle="leeto")
