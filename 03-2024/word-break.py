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
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for w in wordDict:
                if i + 1 - len(w) >= 0 and s[i + 1 - len(w):i + 1] == w:
                    if i + 1 - len(w) == 0 or dp[i - len(w)]:
                        dp[i] = True
        return dp[-1]


solution = Solution().wordBreak
solution(s="leetcode", wordDict=["leet", "code"])
solution(s="applepenapple", wordDict=["apple", "pen"])
solution(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
