import sys


def solution(nums):
    ret = -sys.maxsize
    if not nums:
        return 0
    n = len(nums)
    max_v = min_v = None
    for i in range(1, n + 1):
        if nums[i - 1] > 0:
            if not max_v:
                max_v = nums[i - 1]
            else:
                max_v = max_v * nums[i - 1]
            if min_v:
                min_v = min_v * nums[i - 1]
        elif nums[i - 1] < 0:
            if not min_v:
                min_v = nums[i - 1]
            else:
                min_v = max_v * nums[i - 1]
            if max_v:
                max_v = min_v * nums[i - 1]
        else:
            max_v = min_v = None
        # print(min_v, max_v)
        ret = max(ret, max_v)
    return ret


print(solution([2, 3, -2, 4]))
