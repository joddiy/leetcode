from tools import *


@print_
def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    n, m = len(s), len(s)  # length, start
    dp = [[0] * m for _ in range(n + 1)]
    max_ = 0
    max_s = ""
    for i in range(1, n + 1):  # length
        for j in range(0, n - i + 1):  # start
            if i == 1:
                dp[i][j] = 1
            elif i == 2 and s[j] == s[j + 1]:
                dp[i][j] = 2
            elif s[j] == s[j + i - 1] and dp[i - 2][j + 1]:
                dp[i][j] = dp[i - 2][j + 1] + 2
            if dp[i][j] > max_:
                max_ = dp[i][j]
                max_s = s[j:j + i]
    return max_s


longestPalindrome("babad")
longestPalindrome("cbbd")
longestPalindrome("a")
longestPalindrome("ac")