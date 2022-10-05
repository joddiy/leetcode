def solution(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1
    if i > 0:
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[:i:-1]
    else:
        nums[::] = nums[::-1]


# print(solution([1, 2, 3]))
print(solution([3, 2, 1]))
# print(solution([1, 1, 5]))
print(solution([1, 1]))
# print(solution([1, 5, 8, 4, 7, 6, 5, 3, 1]))
# print(solution([1, 5, 8, 4, 7, 6, 5, 3, 1]))
