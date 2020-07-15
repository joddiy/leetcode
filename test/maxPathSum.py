from utils.tools import *
import sys


def solution(root):
    max_v = -sys.maxsize

    def recursive(root):
        nonlocal max_v
        if not root:
            return 0
        else:
            left = recursive(root.left)
            right = recursive(root.right)
            max_v = max(max_v, left + right + root.val)
            return max(left + root.val, right + root.val, 0)

    recursive(root)
    return max_v


# print(solution(stringToTreeNode("[1,2,3]")))
# print(solution(stringToTreeNode("[1,2,-3]")))
print(solution(stringToTreeNode("[-10,9,20,null,null,15,7]")))
print(solution(stringToTreeNode("[-3]")))