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
            for idx, w in enumerate(wordDict):
                if i >= len(w) - 1 and s[i + 1 - len(w):i +
                                         1] == w and dp[i + 1 - len(w)]:
                    if dp[i + 1] is False:
                        dp[i + 1] = []
                    dp[i + 1].append((idx, len(w)))
        dp[0] = ""
        ret = []

        def create(idx, suffix):
            if idx == 0:
                ret.append(" ".join(wordDict[i] for i in suffix))
                return
            for i, l in dp[idx]:
                create(idx - l, [i] + suffix)

        if dp[-1]:
            create(len(s), [])

        return ret


solution = Solution().wordBreak

solution("catsanddog", ["cat", "cats", "and", "sand", "dog"])
solution("pineapplepenapple",
         ["apple", "pen", "applepen", "pine", "pineapple"])
solution("catsandog", ["cats", "dog", "sand", "and", "cat"])
solution("", ["cats", "dog", "sand", "and", "cat"])
solution("catsandog", [])
solution("", [])