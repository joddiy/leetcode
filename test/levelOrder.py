from utils.tools import *


def solution(root):
    ret = []

    def recursion(root, level):
        if not root:
            return
        if level > len(ret) - 1:
            ret.append([])
        ret[level].append(root.val)
        recursion(root.left, level + 1)
        recursion(root.right, level + 1)

    recursion(root, 0)
    return ret


def solution(root):
    ret = []

    queue = [(0, root)]
    while queue:
        level, node = queue.pop(0)
        if not node:
            continue
        if level > len(ret) - 1:
            ret.append([])
        ret[level].append(node.val)
        queue.extend([(level + 1, node.left), (level + 1, node.right)])
    return ret


print(solution(stringToTreeNode("[3,9,20,null,null,15,7]")))