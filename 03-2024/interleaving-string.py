import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if m < n:
            s1, s2, m, n = s2, s1, n, m
        if n == 0:
            return s1 == s3
        dp = [[False] * (n + 1) for _ in range((m + 1))]
        for i in range(m + 1):  # s1 idx+1
            for j in range(n + 1):  # s2 idx+1
                if i == 0 or j == 0:
                    dp[i][j] = True
                else:
                    if s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                        dp[i][j] = True
                    if s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                        dp[i][j] = True
        return dp[-1][-1]


solution = Solution().isInterleave
solution(s1="aabcc", s2="dbbca", s3="aadbbcbcac")
solution(s1="aabcc", s2="dbbca", s3="aadbbbaccc")
solution(s1="", s2="", s3="")
