def solution(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for w in wordDict:
            if i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w:
                dp[i] = True
    return dp[-1]


print(solution("leetcode", ["leet", "code"]))