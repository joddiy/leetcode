import pprint
from tools import *


class Solution(object):
    @print_
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l, o = 0, 0
        while l < len(haystack) - len(needle) + 1:
            while o < len(needle):
                if haystack[l + o] == needle[o]:
                    o += 1
                else:
                    o = 0
                    break
            if o == len(needle):
                return l
            else:
                l += 1
        return -1


solution = Solution().strStr
# solution(haystack="sadbutsad", needle="sad")
# solution(haystack="leetcode", needle="leeto")
# solution(haystack="ssadbutsad", needle="sad")
solution(haystack="baaaa", needle="aaaa")
