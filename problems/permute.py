from tools import *


@print_
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []
    ret = []

    def recursive(current, remaining):
        if not remaining:
            ret.append(current)
        for i in range(len(remaining)):
            recursive(current + [remaining[i]],
                      remaining[:i] + remaining[i + 1:])

    recursive([], nums)
    return ret


permute([1, 2, 3])
