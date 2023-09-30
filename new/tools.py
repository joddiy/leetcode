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
        if isinstance(result, ListNode):
            result = listNodeToString(result)
        elif isinstance(result, TreeNode):
            result = treeNodeToString(result)
        pprint.pprint(result)
        return result

    return wrapper
