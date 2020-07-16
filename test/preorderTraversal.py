from utils.tools import *


def solution(root):
    res = []

    def recursive(root):
        if not root:
            return
        res.append(root.val)
        recursive(root.left)
        recursive(root.right)
    
    recursive(root)
    return res


print(solution(stringToTreeNode("[1,null,2,3]")))
print(solution(stringToTreeNode("[]")))