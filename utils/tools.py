# -*- coding: utf-8 -*-
# file: tools.py
# author: joddiyzhang@gmail.com
# time: 2018/11/22 10:01 PM
# ------------------------------------------------------------------------

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
                stack.extend([(node.right, False), (node, True), (node.left, False)])
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
                stack.extend([(node.right, False), (node.left, False), (node, True)])
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
                stack.extend([(node, True), (node.right, False), (node.left, False)])
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


def stringToListNode(input):
    import json
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