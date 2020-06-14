from collections import defaultdict


class Node:

    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def solution(head):
    node_dict = defaultdict(Node)

    def build(node):
        if not node:
            return None
        _node = Node(node.val)
        node_dict[node] = _node
        if node.random:
            if node.random in node_dict:
                _node.random = node_dict[node.random]
            else:
                _node.random = build(node.random)
        if node.next:
            if node.next in node_dict:
                _node.next = node_dict[node.next]
            else:
                _node.next = build(node.next)
        return _node

    return build(head)


def solution(head):
    if not head:
        return None

    node_dict = defaultdict(Node)

    _head = Node(head.val)
    node_dict[head] = _head
    ret_head = _head
    while head:
        if head.random:
            if head.random not in node_dict:
                node_dict[head.random] = Node(head.random.val)
            _head.random = node_dict[head.random]
        if head.next:
            if head.next not in node_dict:
                node_dict[head.next] = Node(head.next.val)
            _head.next = node_dict[head.next]
        head = head.next
        _head = _head.next

    return ret_head