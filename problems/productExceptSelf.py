def solution(nums):
    res = [1] * len(nums)
    p = 1
    for i in range(len(nums)):
        res[i] = p
        p *= nums[i]

    right = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res


print(solution([1, 2, 3, 4]))
