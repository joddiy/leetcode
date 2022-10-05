from tools import *


@print_
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)
    cur_v = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] != cur_v:
            cur_v = nums[i]
            i += 1
        else:
            nums.pop(i)
    return len(nums)


removeDuplicates([])
removeDuplicates([1])
removeDuplicates([1, 1, 2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])