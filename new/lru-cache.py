import math
import pprint
from tools import *
from collections import defaultdict


class ListNode(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.pre = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.node_map = {}

    def insert(self, node):
        # insert the node into the head
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node
        node.next.pre = node
        self.node_map[node.key] = node

    def remove(self, node):
        # remove the node from the list
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = node.pre = None
        self.node_map.pop(node.key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map:
            return -1
        else:
            # remove the node from the list
            node = self.node_map[key]
            self.remove(node)
            # insert the node into the head
            self.insert(node)
            return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.node_map:
            self.remove(self.node_map[key])
        # remove a node from the tail
        elif len(self.node_map) == self.capacity:
            self.remove(self.tail.pre)
        # insert the node into the head
        self.insert(ListNode(key, value))


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
print(listNodeToString(obj.head))
obj.put(2, 2)
print(listNodeToString(obj.head))
print(obj.get(1))
print(listNodeToString(obj.head))
obj.put(3, 3)
print(listNodeToString(obj.head))
print(obj.get(2))
print(listNodeToString(obj.head))
obj.put(4, 4)
print(listNodeToString(obj.head))
print(obj.get(1))
print(listNodeToString(obj.head))
print(obj.get(3))
print(listNodeToString(obj.head))
print(obj.get(4))
print(listNodeToString(obj.head))
