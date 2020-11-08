from tools import *


@print_
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    def find(i, j):
        if i > j:
            return -1
        m = (i + j) // 2
        m_v = nums[m]

        if m_v == target:
            return m
        # target at non-axis side (left)
        elif nums[i] <= target < nums[m]:
            return find(i, m - 1)
        # target at non-axis side (right)
        elif nums[m] < target <= nums[j]:
            return find(m + 1, j)
        # target at axis side (left)
        elif nums[i] > nums[m]:
            return find(i, m - 1)
        else:
            return find(m + 1, j)

    return find(0, len(nums) - 1)


search([4, 5, 6, 7, 0, 1, 2], 0)
search([6, 7, 0, 1, 2, 4, 5], 0)
search([5, 6, 7, 0, 1, 2, 4], 0)
search([4, 5, 6, 7, 0, 1, 2], 3)
search([1], 0)
search([5, 1, 3], 3)