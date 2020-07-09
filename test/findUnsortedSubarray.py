def solution(nums):
    n = len(nums)
    if n <= 1:
        return 0
    right = 0
    cur_max = nums[0]
    for i in range(1, n):
        if nums[i] < cur_max:
            right = i
        cur_max = max(cur_max, nums[i])
        

    cur_min = nums[-1]
    left = len(nums)-1
    for i in range(n - 2, -1, -1):
        if nums[i] > cur_min:
            left = i
        cur_min = min(cur_min, nums[i])
    return max(right - left + 1, 0)


# print(solution([2, 6, 4, 8, 10, 9, 15]))
# print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 2, 2]))
