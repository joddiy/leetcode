class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        d = [False] * (n+1)
        d[0] = True
        for i in range(1, n+1):
            for w in wordDict:
                if d[i-len(w)] and s[i-len(w):i] == w:
                    d[i] = True
        return d[-1]


print(Solution().wordBreak(s="catsandog", wordDict=[
      "cats", "dog", "sand", "and", "cat"]))
