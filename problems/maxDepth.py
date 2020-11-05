from utils.tools import *


def solution(root):
    ret = 0

    def recursion(root, level):
        if not root:
            return
        ret = max(ret, level + 1)
        recursion(root.left, level + 1)
        recursion(root.right, level + 1)

    recursion(root, 0)
    return ret


def solution(root):
    ret = 0

    queue = [(0, root)]
    while queue:
        level, node = queue.pop(0)
        if not node:
            continue
        ret = max(ret, level + 1)
        queue.extend([(level + 1, node.left), (level + 1, node.right)])
    return ret


print(solution(stringToTreeNode("[3,9,20,null,null,15,7]")))