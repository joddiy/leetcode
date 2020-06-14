def solution(nums):
    ret = nums[0]
    for idx in range(1, len(nums)):
        ret ^= nums[idx]

    return ret


print(solution([2, 2, 1]))
