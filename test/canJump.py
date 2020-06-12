def solution(nums):
    i, max_i = 0, 0
    while i <= max_i and i < len(nums) and max_i < len(nums) - 1:
        max_i = max(max_i, i + nums[i])
        i += 1
    return max_i >= len(nums) - 1


print(solution([2, 3, 1, 1, 4]))
# print(solution([3, 2, 1, 0, 4]))
print(solution([2]))
