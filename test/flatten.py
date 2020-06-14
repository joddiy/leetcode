from utils.tools import *


def solution(root):

    def flatten(root):
        if not root.left and not root.right:
            return root
        if root.left:
            deepest = flatten(root.left)
            deepest.right = root.right
            root.right = root.left
            root.left = None
        if root.right:
            return flatten(root.right)

    flatten(root)
    return root


print(treeNodeToString(solution(stringToTreeNode("[1,2,5,3,4,6]"))))