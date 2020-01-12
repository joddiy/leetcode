class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_ret = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i) # last invalid point
                else:
                    max_ret = max(max_ret, i - stack[-1]) # i-stack[-1] is current valid length
        return max_ret

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxans = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] ==')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >=2 else 0) + 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0) + 2
                maxans = max(maxans, dp[i])
        return maxans


# print(Solution().longestValidParentheses(")()())"))
# print(Solution().longestValidParentheses("(()"))
# print(Solution().longestValidParentheses("()(()"))
print(Solution().longestValidParentheses(")()())"))
