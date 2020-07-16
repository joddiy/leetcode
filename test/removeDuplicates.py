def solution(nums):
    cur_val = None
    ret = 0
    i = 0
    while i < len(nums):
        num = nums[i]
        if num != cur_val:
            ret += 1
            cur_val = num
            i += 1
        else:
            nums.pop(i)
    return ret

print(solution([]))
print(solution([1]))
print(solution([1, 1, 2]))
