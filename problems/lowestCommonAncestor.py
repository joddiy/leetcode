from utils.tools import *


def solution(root, p, q):
    low_desc = None

    def recursive(root):
        nonlocal low_desc
        if not root:
            return 0
        ret = recursive(root.left)
        if ret < 2:
            ret += recursive(root.right)
        if root.val in (q.val, p.val):
            ret += 1
        if ret == 2 and not low_desc:
            low_desc = root
        return ret

    recursive(root)
    return low_desc


print(
    solution(stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"), ListNode(5),
             ListNode(1)).val)
print(
    solution(stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"), ListNode(5),
             ListNode(4)).val)