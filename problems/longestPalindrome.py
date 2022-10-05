from tools import *


class Solution(object):
    # O(n^2), dp
    @print_
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_ = 0
        ret = ""
        dp = [[0] * n for _ in range(n + 1)]  # length * start_point
        for l in range(1, n + 1):  # length from 1 to n
            for i in range(n - l + 1):  # start point from 0 to n-l
                if l == 1:
                    dp[l][i] = 1
                elif l == 2 and s[i] == s[i + 1]:
                    dp[l][i] = 2
                elif s[i] == s[i + l - 1] and dp[l - 2][i + 1]:
                    dp[l][i] = dp[l - 2][i + 1] + 2
                if dp[l][i] > max_:
                    max_ = dp[l][i]
                    ret = s[i:i + l]
        return ret

    # O(n^2)?, slide window
    @print_
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # for example, for 'a, bab, bbabb'
        # at the 'bab', we update maxlength as 3
        # at the 'bbabb', we update maxlength as 5
        # ffor 'aa, baab, bbaabb'
        # at the 'aa', we update maxlength as 2
        # at the 'baab', we update maxlength as 4
        # at the 'bbaabb', we update maxlength as 6
        if len(s) < 2 or s == s[::-1]:
            return s
        start, maxlength = 0, 1
        for i in range(len(s)):
            odd = s[i - maxlength - 1:i + 1] # 2 + maxlength
            even = s[i - maxlength:i + 1] # 1 + maxlength
            if i - maxlength - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlength - 1
                maxlength += 2
                print('odd', end="")
            elif i - maxlength >= 0 and even == even[::-1]:
                start = i - maxlength
                maxlength += 1
                print('even', end="")
            print(i, odd, even, start, maxlength)
        return s[start:start + maxlength]


solution = Solution().longestPalindrome

solution("dbbabbad")
# solution("cbbd")
# solution("a")
# solution("ac")