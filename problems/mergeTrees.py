from utils.tools import *


def solution(t1, t2):

    def recursive(t1, t2):
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        else:
            t1.left = recursive(t1.left, t2.left)
            t1.right = recursive(t1.right, t2.right)
            t1.val = t1.val + t2.val
            return t1

    return recursive(t1, t2)


print(
    treeNodeToString(
        solution(stringToTreeNode("[1,3,2,5]"),
                 stringToTreeNode("[2,1,3,null,4,null,7]"))))
