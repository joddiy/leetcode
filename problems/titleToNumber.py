from tools import *


class Solution(object):
    @print_
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for w in s:
            ret *= 26
            ret += ord(w) - 64
        return ret


solution = Solution().titleToNumber

solution("A")
solution("AB")
solution("ZY")