from utils.tools import *


def solution(root):

    def recursive(root):
        if root:
            root.left, root.right = recursive(root.right), recursive(root.left)
        return root

    return recursive(root)


print(treeNodeToString(solution(stringToTreeNode("[4,2,7,1,3,6,9]"))))