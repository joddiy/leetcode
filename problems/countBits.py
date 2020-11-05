def solution(num):
    dp = [0] * (num + 1)
    for i in range(1, num + 1):
        dp[i] = dp[i // 2] + i % 2
    return dp


print(solution(2))
print(solution(5))
