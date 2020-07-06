from utils.tools import *


# O(H + k)
def solution(root, k):
    found = None

    def recursive(root, i):
        nonlocal found
        if not root:
            return i
        i = recursive(root.left, i) + 1
        if i == k:
            found = root.val
            return i
        elif found is not None:
            return i
        elif i < k:
            return recursive(root.right, i)

    recursive(root, 0)
    return found


# O(H + k)
def solution(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right


# print(solution(stringToTreeNode("[3,1,4,null,2]"), 1))
print(solution(stringToTreeNode("[3]"), 1))
# print(solution(stringToTreeNode("[5,3,6,2,4,null,null,1]"), 3))