class Solution(object):

    # dp O(n^2)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 or s == s[::-1]:
            return s
        m = len(s)
        dp = [[0] * m for _ in range(m)]
        ret = 0
        ret_pos = set()
        for i in range(m):
            if i + 1 < m:
                dp[i][i+1] = 2 if s[i] == s[i+1] else 0  # even
            dp[i][i] = 1  # odd
        for i in range(m):  # i is the length of the slide window
            for j in range(m):  # j is the start point of slide window
                if j + i >= m:
                    break
                if i == 0:  # for the length of window is zero
                    dp[j][j+i] = 1
                # for each slide windor, grow from the sub-problem
                elif dp[j+1][j+i-1] > 0 and s[j] == s[j+i]:
                    dp[j][j+i] = dp[j+1][j+i-1] + 2
                if dp[j][j+i] > ret:  # update the max length
                    ret = dp[j][j+i]
                    ret_pos = (j, j+i)
        return s[ret_pos[0]:ret_pos[1]+1]
 
    # O(n^2)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 or s == s[::-1]:
            return s
        start, maxlength = 0, 1
        for i in range(len(s)):
            odd = s[i-maxlength-1:i+1]
            even = s[i-maxlength:i+1]
            if i-maxlength-1 >= 0 and odd == odd[::-1]:
                start = i-maxlength-1
                maxlength += 2
            elif i-maxlength >= 0 and even == even[::-1]:
                start = i-maxlength
                maxlength += 1
        return s[start:start+maxlength]


print(Solution().longestPalindrome("ababbaba"))
