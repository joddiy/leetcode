from utils.tools import *


def solution(preorder, inorder):

    inorder_dict = {v: k for k, v in enumerate(inorder)}

    def build(i, j):
        if not preorder or i > j:
            return None
        val = preorder.pop(0)
        key = inorder_dict[val]
        node = TreeNode(val)
        node.left = build(i, key - 1)
        node.right = build(key + 1, j)
        return node

    return build(0, len(inorder) - 1)


print(treeNodeToString(solution([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
