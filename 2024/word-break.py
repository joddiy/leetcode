import math
import sys

from tools import *
import pprint
from collections import defaultdict


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
                if i - lw + 1 >= 0 and s[i - lw + 1:i + 1] == w:
                    if i - lw < 0 or dp[i - lw] == True:
                        dp[i] = True
        return dp[-1]


solution = Solution().wordBreak
solution(s="leetcode", wordDict=["leet", "code"])
solution(s="applepenapple", wordDict=["apple", "pen"])
solution(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
