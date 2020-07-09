from utils.tools import *


def solution(root):

    def recusive(root):
        nonlocal ret
        if not root:
            return 0, 0

        l = recusive(root.left)
        r = recusive(root.right)
        ret = max(ret, max(l) + max(r))
        return max(l) + 1, max(r) + 1

    ret = 0
    recusive(root)
    return ret


print(solution(stringToTreeNode("[1,2,3,4,5]")))