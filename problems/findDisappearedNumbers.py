def solution(nums):
    n = len(nums)
    for i in range(n):
        _num = abs(nums[i])
        if _num <= n:
            nums[_num - 1] = -abs(nums[_num - 1])

    ret = []
    for i in range(n):
        if nums[i] > 0:
            ret.append(i + 1)
    return ret


print(solution([4, 3, 2, 7, 8, 2, 3, 1]))
