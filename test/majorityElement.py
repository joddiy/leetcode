def solution(nums):
    cur_value = nums[0]
    cur_num = 1
    for num in nums[1:]:
        if num != cur_value:
            cur_num -= 1
            if cur_num == -1:
                cur_value = num
                cur_num = 1
        else:
            cur_num += 1
    return cur_value


print(solution([2, 2, 1, 1, 1, 2, 2]))
