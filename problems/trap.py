from tools import *


@print_
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
        return 0
    height = [0] + height + [0]
    n = len(height)
    left, right = [0] * n, [0] * n
    # left
    max_ = 0
    for i in range(n):
        max_ = max(max_, height[i])
        left[i] = max_
    max_ = 0
    for i in range(n - 1, -1, -1):
        max_ = max(max_, height[i])
        right[i] = max_
    ret = 0
    for i in range(n):
        ret += min(left[i], right[i]) - height[i]
    return ret


trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
trap([4, 2, 0, 3, 2, 5])
