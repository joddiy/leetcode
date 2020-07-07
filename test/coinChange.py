def solution(coins, amount):
    if len(coins) == 0:
        return -1
    if amount == 0:
        return 0

    coins = sorted(set(coins), reverse=True)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i == c:
                dp[i] = 1
                break
            elif i > c and dp[i - c] > 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return -1 if dp[-1] > amount else dp[-1]


# print(solution([1, 2, 5], 11))
# print(solution([2], 3))
print(solution([1], 0))