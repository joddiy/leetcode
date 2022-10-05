# -*- coding: utf-8 -*-
# file: tools.py
# author: joddiyzhang@gmail.com
# time: 2018/11/22 10:01 PM
# ------------------------------------------------------------------------
import json
from functools import wraps
import pprint


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.val < other.val


def GenerateTree(list):
    pass


def BFS(root):
    queue = [root]
    output = []
    while queue:
        node = queue.pop(0)
        if node:
            output.append(node.val)
            queue.extend([node.left, node.right])
    return output


def inorderIterative(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # p = root
    # stack = []
    # output = []
    # while p or stack:
    #     while p:
    #         stack.append(p)
    #         p = p.left  # first, go to the deepest left
    #     if stack:
    #         p = stack.pop()
    #         output.append(p.val)  # output the top of stack
    #         p = p.right  # take one right node
    #         # when right is None, will pop a new node at next iteration
    # return output

    output = []
    stack = [(root, False)]
    while stack:
        node, label = stack.pop()
        if node:
            if label:
                output.append(node.val)
            else:
                stack.extend([(node.right, False), (node, True),
                              (node.left, False)])
    return output


def preorderIterative(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # p = root
    # stack = []
    # output = []
    # while p or stack:
    #     while p:
    #         output.append(p.val)
    #         stack.append(p)
    #         p = p.left
    #     if stack:
    #         p = stack.pop()
    #         p = p.right
    #
    # return output

    # output = []
    # stack = [root]
    # while stack:
    #     node = stack.pop()
    #     if node:
    #         output.append(node.val)
    #         stack.extend([node.right, node.left])
    # return output

    output = []
    stack = [(root, False)]
    while stack:
        node, label = stack.pop()
        if node:
            if label:
                output.append(node.val)
            else:
                stack.extend([(node.right, False), (node.left, False),
                              (node, True)])
    return output


def postorderIterative(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    output = []
    stack = [(root, False)]
    while stack:
        node, label = stack.pop()
        if node:
            if label:
                output.append(node.val)
            else:
                stack.extend([(node, True), (node.right, False),
                              (node.left, False)])
    return output


def inorderRecursive(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def recursive(root, res):
        if root:
            recursive(root.left, res)
            res.append(root.val)
            recursive(root.right, res)

    res = []
    recursive(root, res)
    return res


def preorderRecursive(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def recursive(root, res):
        if root:
            res.append(root.val)
            recursive(root.left, res)
            recursive(root.right, res)

    res = []
    recursive(root, res)
    return res


def postorderRecursive(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def recursive(root, res):
        if root:
            recursive(root.left, res)
            recursive(root.right, res)
            res.append(root.val)

    res = []
    recursive(root, res)
    return res


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


# 最长公共子串
def getLCS1(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * n for _ in range(m)]
    ret = 0
    for i in range(m):
        dp[i][0] = 1 if str1[i] == str2[0] else 0
    for j in range(n):
        dp[0][j] = 1 if str1[0] == str2[j] else 0
    for i in range(1, m):
        for j in range(1, n):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            ret = max(ret, dp[i][j])
    return ret


# 最长公共子序列
def getLCS2(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


# 快排
def partition(arr, low, high):
    m = (low + high) // 2
    # swap the mid with first
    arr[low], arr[m] = arr[m], arr[low]
    pivot = low
    index = pivot + 1 # the first value larger than pivot
    i = index
    while i <= high:
        if arr[i] < arr[pivot]:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
        i += 1
    # swap the pivot to the index - 1
    arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
    return index-1

def quicksort(arr, low, high):
    if low > high:
        return

    pi = partition(arr, low, high)
    quicksort(arr, low, pi-1)
    quicksort(arr, pi+1, high)
    return arr

return quicksort(arr, 0, len(arr)-1)


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i])


def list_node(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_ = []
        for a in args:
            if isinstance(
                    a, str) and len(a) >= 2 and a[0] == '[' and a[-1] == ']':
                args_.append(stringToListNode(a))
            else:
                args_.append(a)
        kwargs_ = {}
        for k, a in kwargs.items():
            if isinstance(
                    a, str) and len(a) >= 2 and a[0] == '[' and a[-1] == ']':
                kwargs_[k] = stringToListNode(a)
            else:
                kwargs_[k] = a
        result = func(*args_, **kwargs_)
        if isinstance(result, tuple):
            result_ = []
            for r in result:
                if isinstance(r, ListNode):
                    result_.append(listNodeToString(r))
                else:
                    result_.append(r)
            return tuple(result_)
        else:
            if isinstance(result, ListNode):
                result = listNodeToString(result)
            return result

    return wrapper


def tree_node(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_ = []
        for a in args:
            if isinstance(
                    a, str) and len(a) >= 2 and a[0] == '[' and a[-1] == ']':
                args_.append(stringToTreeNode(a))
            else:
                args_.append(a)
        kwargs_ = {}
        for k, a in kwargs.items():
            if isinstance(
                    a, str) and len(a) >= 2 and a[0] == '[' and a[-1] == ']':
                kwargs_[k] = stringToTreeNode(a)
            else:
                kwargs_[k] = a
        result = func(*args_, **kwargs_)
        if isinstance(result, tuple):
            result_ = []
            for r in result:
                if isinstance(r, TreeNode):
                    result_.append(treeNodeToString(r))
                else:
                    result_.append(r)
            return tuple(result_)
        else:
            if isinstance(result, TreeNode):
                result = treeNodeToString(result)
            return result

    return wrapper


def print_(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        pprint.pprint(result)
        return result

    return wrapper