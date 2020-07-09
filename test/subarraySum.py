# O(n^2)
def solution(nums, k):
    n = len(nums)
    ret = 0
    dp = [[0] * (n + 1) for _ in range(n)]  # (start_pos, len)
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            if i == 1:
                dp[j][i] = nums[j]
            else:
                dp[j][i] = nums[j] + dp[j + 1][i - 1]
            if dp[j][i] == k:
                ret += 1
    return ret

# O(n)
def solution(nums, k):
    cache = {0: 1}
    cur_sum = 0
    ret = 0
    for n in nums:
        cur_sum += n
        ret += cache.get(cur_sum - k, 0)
        cache[cur_sum] = cache.get(cur_sum, 0) + 1
    return ret


print(solution([1, 1, 1], 2))
print(solution([1], 1))
