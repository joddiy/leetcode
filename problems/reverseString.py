from tools import *


class Solution(object):
    @print_
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
        return s

solution = Solution().reverseString

solution(["h", "e", "l", "l", "o"])
