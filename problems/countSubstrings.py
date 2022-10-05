from tools import *


class Solution(object):
    @print_
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n + 1)]  # (len, start_pos)
        ret = 0
        for i in range(1, n + 1):
            for j in range(0, n - i + 1):
                if i == 1 or i == 2 and s[j] == s[j + 1]:
                    dp[i][j] = 1
                    ret += 1
                elif s[j] == s[j + i - 1] and dp[i - 2][j + 1]:
                    dp[i][j] = 1
                    ret += 1
        return ret


solution = Solution().countSubstrings
solution("a")
solution("")
solution("abc")
solution("aaa")