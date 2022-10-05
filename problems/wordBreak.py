from tools import *


class Solution(object):
    @print_
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for w in wordDict:
                if i - len(w) >= 0 and s[i-len(w):i] == w and dp[i - len(w)]:
                    dp[i] = True

        return dp[-1]


solution = Solution().wordBreak

solution("leetcode", ["leet", "code"])
solution("applepenapple", ["apple", "pen"])
solution("catsandog", ["cats", "dog", "sand", "and", "cat"])