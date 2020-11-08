from tools import *


@print_
def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    for i, v in enumerate(nums):
        if v <= 0 or v > n:
            nums[i] = n + 1

    for i, v in enumerate(nums):
        if abs(v) != n + 1:
            l = abs(v) - 1
            nums[l] = -abs(nums[l])

    ret = 0
    while ret < len(nums) and nums[ret] < 0:
        ret += 1
    return ret + 1


firstMissingPositive([3, 4, -1, 1])
firstMissingPositive([1, 2, 0])
firstMissingPositive([7, 8, 9, 11, 12])
firstMissingPositive([1])
firstMissingPositive([1, 2, 3])
