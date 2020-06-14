from utils.tools import *


def solution(root):
    if not root:
        return True

    def recursion(root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and root2:
            if root1.val == root2.val:
                return recursion(root1.left, root2.right) and recursion(
                    root1.right, root2.left)
            else:
                return False
        else:
            return False

    return recursion(root.left, root.right)


def solution(root):
    if not root:
        return True
    queue1 = [root.left, root.right]
    queue2 = [root.right, root.left]

    while queue1 and queue2:
        node1 = queue1.pop(0)
        node2 = queue2.pop(0)
        if not node1 and not node2:
            continue
        elif node1 and node2 and node1.val == node2.val:
            queue1.extend([node1.left, node1.right])
            queue2.extend([node2.right, node2.left])
        else:
            return False
    if not queue1 and not queue2:
        return True
    else:
        return False


print(solution(stringToTreeNode("[1,2,2,3,4,4,3]")))
print(solution(stringToTreeNode("[1,2,3]")))