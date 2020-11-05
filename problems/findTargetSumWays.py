def solution(nums, S):
    sum_v = sum(nums)
    if sum_v < S: 
        return 0
    n = len(nums)
    dp = [0] * (2 * sum_v + 1)
    dp[nums[0]] += 1
    dp[-nums[0]] += 1
    for n in nums[1:]:
        _dp = [0] * (2 * sum_v + 1)
        for i in range(-sum_v, sum_v + 1):
            if i + n <= sum_v:
                _dp[i] += dp[i + n]
            if i - n >= -sum_v:
                _dp[i] += dp[i - n]
        dp = _dp
    return dp[S]


print(solution([1, 1, 1, 1, 1], 3))
print(solution([1], 2))