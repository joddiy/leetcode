from utils.tools import *


def solution(root):
    ret = []

    def recursion(root):
        if not root:
            return
        recursion(root.left)
        ret.append(root.val)
        recursion(root.right)

    recursion(root)
    return ret


def solution(root):
    ret = []
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        elif isinstance(node, int):
            ret.append(node)
        else:
            stack.extend([node.right, node.val, node.left])
    return ret


print(solution(stringToTreeNode("[1,null,2,3]")))
