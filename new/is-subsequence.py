from tools import *
import pprint


class Solution(object):
    @print_
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = 0, 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
            j += 1
        return False


solution = Solution().isSubsequence
solution(s="abc", t="ahbgdc")
solution(s="axc", t="ahbgdc")
solution(s="", t="ahbgdc")
