# o(n^2)
def solution(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# O(n * logn)
def solution(nums):
    dp = [0] * len(nums)
    size = 0
    for n in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if dp[m] < n:
                i = m + 1
            else:
                j = m
        dp[i] = n
        size = max(size, i + 1)
    return size


print(solution([10, 9, 2, 5, 3, 7, 101, 18]))
