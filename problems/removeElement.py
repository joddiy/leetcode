def solution(nums, val):
    ret = 0
    i = 0
    while i < len(nums):
        num = nums[i]
        if num != val:
            ret += 1
            i += 1
        else:
            nums.pop(i)
    return ret

print(solution([1, 1, 2], 2))
