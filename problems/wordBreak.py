from tools import *


class Solution(object):
    @print_
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if i >= len(w) - 1 and s[i + 1 - len(w):i + 1] == w:
                    dp[i + 1] = dp[i + 1] or dp[i + 1 - len(w)]
        return dp[-1]


solution = Solution().wordBreak

solution("leetcode", ["leet", "code"])
solution("applepenapple", ["apple", "pen"])
solution("catsandog", ["cats", "dog", "sand", "and", "cat"])