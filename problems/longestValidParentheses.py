from tools import *


class Solution(object):
    # dp O(n)
    @print_
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i - 2 >= 0 else 0) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2]
                                             if i - dp[i - 1] - 2 >= 0 else 0)
                ret = max(ret, dp[i])
        return ret

solution = Solution().longestValidParentheses

solution(")()())")
solution("(()))())(")
