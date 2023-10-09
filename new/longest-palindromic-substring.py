import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # solution O(n^2)
        n = len(s)
        dp = [[0] * n for _ in range(n)]  # (start_pos, len-1)

        max_i, max_l = 0, 0
        for l in range(n):
            for i in range(n - l):
                # print(i, l, s[i:i + l + 1], s[i], s[i + l])
                if l == 0:
                    dp[i][l] = True
                elif l == 1 and s[i] == s[i + l]:
                    dp[i][l] = True
                elif s[i] == s[i + l] and dp[i + 1][l - 2]:
                    dp[i][l] = True
                if dp[i][l] and l > max_l:
                    max_i, max_l = i, l
        return s[max_i:max_i + max_l + 1]

        # solution 2
        # if len(s) < 2 or s == s[::-1]:
        #     return s
        # start, maxlength = 0, 1
        # for i in range(len(s)):
        #     odd = s[i-maxlength-1:i+1]
        #     even = s[i-maxlength:i+1]
        #     if i-maxlength-1 >= 0 and odd == odd[::-1]:
        #         start = i-maxlength-1
        #         maxlength += 2
        #     elif i-maxlength >= 0 and even == even[::-1]:
        #         start = i-maxlength
        #         maxlength += 1
        # return s[start:start+maxlength]


solution = Solution().longestPalindrome
solution(s="babad")
solution(s="cbbd")
