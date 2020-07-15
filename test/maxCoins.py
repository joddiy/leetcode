def solution(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    def recursive(i, j):
        if dp[i][j] or j == i + 1:
            return dp[i][j]
        coins = 0
        for k in range(i + 1, j):
            # we firstly burst (i,k) and (k,j), only leave (i,k,j) three ballons
            coins = max(
                coins,
                nums[i] * nums[k] * nums[j] + recursive(i, k) + recursive(k, j))
        dp[i][j] = coins
        return coins

    return recursive(0, n - 1)


print(solution([3, 1, 5, 8]))
