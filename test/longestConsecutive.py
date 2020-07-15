def solution(nums):
    if not nums:
        return 0
    set_nums = set(nums)
    max_v = 0
    for num in nums:
        if num - 1 not in set_nums:
            count = 1
            while num + 1 in set_nums:
                num += 1
                count += 1
            max_v = max(max_v, count)
    return max_v


print(solution([100, 4, 200, 1, 3, 2]))