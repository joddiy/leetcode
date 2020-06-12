# dp O(n)
def solution(s):
    ret = 0
    dp = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ")":
            print(s[i], i, dp[i-1])
            if s[i-1] == "(":
                dp[i] = (dp[i-2] if i > 1 else 0) + 2
            elif i-dp[i-1] > 0 and s[i-dp[i-1]-1] == "(":
                dp[i] = dp[i-1] + 2 + \
                    (dp[i-dp[i-1]-2] if i-dp[i-1]-2 > 0 else 0)
        ret = max(ret, dp[i])
    return ret


# print(solution(")()())"))
print(solution("(()))())("))

