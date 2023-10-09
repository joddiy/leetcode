import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                lw = len(w)
                # get a valid word of s
                if i >= lw - 1 and s[i - (lw - 1):i + 1] == w:
                    # previous sub-string is valid
                    if i - (lw - 1) - 1 < 0 or dp[i - (lw - 1) - 1]:
                        dp[i] = True
        return dp[-1]


solution = Solution().wordBreak
solution(s="leetcode", wordDict=["leet", "code"])
solution(s="applepenapple", wordDict=["apple", "pen"])
solution(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
