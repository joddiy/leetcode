def solution(nums):
    sum_v = sum(nums)
    if sum_v % 2 == 1:
        return False
    if max(nums) > sum_v // 2:
        return False
    scale = sum_v // 2 + 1
    dp = [[False] * scale for _ in range(len(nums))]

    nums = sorted(nums, reverse=True)
    dp[0][nums[0]] = True
    for i in range(1, len(nums)):
        dp[i][nums[i]] = True
        for j in range(scale - 1, 0, -1):
            if dp[i - 1][j]:
                dp[i][j] = True
            if j > nums[i] and dp[i - 1][j - nums[i]]:
                dp[i][j] = True
            if dp[i][-1]:
                return True
    return dp[-1][-1]


def solution(nums):

    def recursive(nums, target):
        for i, num in enumerate(nums):
            if num > target:
                return False
            elif num == target:
                return True
            elif recursive(nums[i + 1:], target - nums[i]):
                return True
        return False

    sum_v = sum(nums)
    if sum_v % 2 == 1:
        return False
    nums = sorted(nums, reverse=True)
    return recursive(nums, sum_v // 2)


# print(solution([1, 5, 11, 5]))
# print(solution([1, 2, 3, 5]))
# print(solution([1, 2, 5]))
print(solution([2, 2, 3, 5]))
