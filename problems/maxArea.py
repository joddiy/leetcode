from tools import *


@print_
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height or len(height) == 1:
        return 0
    i, j = 0, len(height) - 1
    max_ = 0
    while i < j:
        max_ = max(min(height[i], height[j]) * (j - i), max_)
        if height[i] < height[j]:
            k = i + 1
            while k < j and height[k] < height[i]:
                k += 1
            i = k
        else:
            k = j - 1
            while k > i and height[k] < height[j]:
                k -= 1
            j = k
        print(i, j)
    return max_


maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
maxArea([1, 1])
maxArea([2, 3, 4, 5, 18, 17, 6])
maxArea([4, 3, 2, 1, 4])
maxArea([1, 2, 1])
