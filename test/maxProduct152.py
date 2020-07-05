def solution(nums):
    maximum = b = s = nums[0]
    for num in nums[1:]:
        b, s = max(num, b * num, s * num), min(num, b * num, s * num)
        maximum = max(maximum, b)
    return maximum


# print(solution([2, 3, -2, 4]))
print(solution([-2, 0, -1]))