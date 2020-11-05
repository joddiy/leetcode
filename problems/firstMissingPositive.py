def solution(nums):
    nums.append(0)
    n = len(nums)
    for i in range(n):
        if nums[i] < 0 or nums[i] > n - 1:
            nums[i] = 0
    for i in range(n):
        nums[nums[i] % n] += n
    for i in range(1, n):
        if nums[i] < n:
            return i
    return n


# print(solution([3, 4, -1, 1]))
# print(solution([1, 2, 0]))
# print(solution([7, 8, 9, 11, 12]))
print(solution([1]))
