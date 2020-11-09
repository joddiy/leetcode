from tools import *


class Solution(object):
    # O(m^k), k is the # of '*'
    @print_
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        memo = {}

        def match(i, j):
            if (i, j) not in memo:
                if j == n:
                    # once pattern ends
                    # the string should end too
                    res = i == m
                else:
                    if p[j] == '*':
                        # try empty sequence
                        res = match(i, j + 1)
                        # try each possible sequence
                        for i_ in range(i, m):
                            res = res or match(i_ + 1, j)
                    elif i < m and p[j] in ('?', s[i]):
                        res = match(i + 1, j + 1)
                    else:
                        res = False
                memo[(i, j)] = res
            return memo[(i, j)]

        return match(0, 0)

    # O(m * n)
    @print_
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False] * length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length + 1):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]


solution = Solution().isMatch

# solution("aa", "a")
# solution("aa", "*")
# solution("cb", "?a")
solution("adceb", "*a*b")