def solution(nums):
    if not nums:
        return 0
    dp = [[0, 0] for _ in range(len(nums))]  # (rob, not_rob) * n
    dp[0][0], dp[0][1] = nums[0], 0
    for i in range(1, len(nums)):
        dp[i][0] = dp[i - 1][1] + nums[i]
        dp[i][1] = max(dp[i - 1])
    return max(dp[-1])


def solution(nums):
    last, now = 0, 0
    for i in nums:
        last, now = now, max(last + i, now)
    return now


# print(solution([1, 2, 3, 1]))
# print(solution([2, 7, 9, 3, 1]))
print(solution([]))
