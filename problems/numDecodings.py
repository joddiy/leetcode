from tools import *


class Solution(object):
    @print_
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        # set the first one for the first dp[i-2]
        dp[0] = 1
        # set this zero for string starting with zeros
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, n + 1):
            # one-step
            if 0 < int(s[i - 1:i]) <= 9:
                dp[i] += dp[i - 1]
            # two-step
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp


solution = Solution().numDecodings

# solution("12")
# solution("226")
# solution("326")
# solution("1")

# solution("206")
# solution("20")
# solution("0")
# solution("00")
# solution("002")
# solution("2101")
solution("1123")