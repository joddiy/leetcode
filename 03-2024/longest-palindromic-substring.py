import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ret = ""
        for i in range(n):  # len - 1
            for j in range(n - i):  # start
                if i == 0:
                    dp[i][j] = True
                elif i == 1 and s[j] == s[j + 1]:
                    dp[i][j] = True
                elif s[j] == s[j + i] and dp[i - 2][j + 1]:
                    dp[i][j] = True
                if dp[i][j] and (i + 1) > len(ret):
                    ret = s[j:j + i + 1]
        return ret


solution = Solution().longestPalindrome
solution(s="babad")
solution(s="cbbd")
