from utils.tools import *


def solution(root):

    def recursive(root):
        if not root:
            return 0, 0

        l_rob, l_not_rob = recursive(root.left)
        r_rob, r_not_rob = recursive(root.right)
        rob = l_not_rob + r_not_rob + root.val
        not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)
        return rob, not_rob

    return max(recursive(root))


print(solution(stringToTreeNode("[3,2,3,null,3,null,1]")))
print(solution(stringToTreeNode("[3,4,5,1,3,null,1]")))