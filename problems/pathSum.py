from utils.tools import *


def solution(root, target):

    def recursive(root, cur_sum):
        if root:
            nonlocal ret
            cur_sum += root.val
            ret += cache.get(cur_sum - target, 0)
            cache[cur_sum] = cache.get(cur_sum, 0) + 1
            recursive(root.left, cur_sum)
            recursive(root.right, cur_sum)
            cache[cur_sum] -= 1

    ret = 0
    cache = {0: 1}
    recursive(root, 0)
    return ret


print(solution(stringToTreeNode("[10,5,-3,3,2,null,11,3,-2,null,1]"), 8))