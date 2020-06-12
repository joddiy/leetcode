from utils.tools import *
import sys


def solution(root):
    if not root:
        return True

    def recursion(root, min_v, max_v):
        if not root:
            return True
        elif root.val <= min_v or root.val >= max_v:
            return False
        else:
            return recursion(root.left, min_v, root.val) and recursion(
                root.right, root.val, max_v)

    return recursion(root.left, -sys.maxsize, root.val) and recursion(
        root.right, root.val, sys.maxsize)


print(solution(stringToTreeNode("[2,1,3]")))
print(solution(stringToTreeNode("[5,1,4,null,null,3,6]")))
