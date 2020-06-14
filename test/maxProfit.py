import sys


def solution(prices):
    cur_min = sys.maxsize
    max_profit = 0
    for p in prices:
        cur_min = min(cur_min, p)
        max_profit = max(max_profit, p - cur_min)
    return max_profit

print(solution([7, 1, 5, 3, 6, 4]))
