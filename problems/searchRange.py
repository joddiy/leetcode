from tools import *


@print_
def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if not nums:
        return (-1, -1)

    # find the first value which is larger
    # or equal than target
    def searchLeft(i, j):
        if j < i:
            return i
        m = (i + j) // 2
        if nums[m] < target:
            return searchLeft(m + 1, j)
        else:
            return searchLeft(i, m - 1)

    # find the first value which is less
    # or equal than target
    def searchRight(i, j):
        if j < i:
            return j
        m = (i + j) // 2
        if nums[m] > target:
            return searchRight(i, m - 1)
        else:
            return searchRight(m + 1, j)

    l, r = searchLeft(0, len(nums) - 1), searchRight(0, len(nums) - 1)
    return (l, r) if l <= r else (-1, -1)


searchRange([5, 7, 7, 8, 8, 10], 8)
searchRange([5, 7, 7, 8, 8, 10], 6)
searchRange([], 0)
