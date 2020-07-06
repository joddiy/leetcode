import math, sys


def solution(n):
    dp = [0] * (n + 1)
    squares = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
    dp[1] = 1
    for i in range(2, n + 1):
        min_v = sys.maxsize
        for j in squares:
            if i - j < 0:
                break
            min_v = min(min_v, dp[i - j])
        dp[i] = min_v + 1
    return dp[-1]

print(solution(12))
print(solution(13))