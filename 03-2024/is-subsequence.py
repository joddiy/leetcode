import sys

from tools import *
import pprint
from collections import Counter


class Solution(object):
    @print_
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


solution = Solution().isSubsequence
solution(s="abc", t="ahbgdc")
solution(s="acb", t="ahbgdc")
solution(s="axc", t="ahbgdc")
