def solution(nums):
    n = len(nums)
    if n == 0 or n == 1:
        return nums
    i = 0
    while i < n and nums[i] != 0:
        i += 1
    j = i
    while True:
        while j < n and nums[j] == 0:
            j += 1
        if j >= n:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    return nums


def solution(nums):
    n = len(nums)
    if n == 0 or n == 1:
        return nums
    i = 0
    while i < n and nums[i] != 0:
        i += 1
    for j in range(i + 1, n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums


print(solution([0, 1, 0, 3, 12]))
print(solution([1, 0, 3, 12]))
print(solution([1]))
print(solution([2, 1]))