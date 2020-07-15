def solution(prices):
    if not prices:
        return 0
    n = len(prices)
    buy, sell, cooldown = [0] * n, [0] * n, [0] * n
    bought = buy[0] = -prices[0]
    for i in range(1, n):
        buy[i] = cooldown[i - 1] - prices[i]
        sell[i] = bought + prices[i]
        cooldown[i] = max(buy[i - 1], sell[i - 1], cooldown[i - 1])
        bought = max(bought, buy[i])
    return max(buy[-1], sell[-1], cooldown[-1])


print(solution([1, 2, 3, 0, 2]))
