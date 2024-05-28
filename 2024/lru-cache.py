import math
import sys

from tools import *
import pprint
from collections import defaultdict


class DListNode(object):
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
        self.capacity = capacity
        self.map_ = {}
        self.list_ = DListNode(None, None)
        self.list_e = DListNode(None, None)
        self.list_.next = self.list_e
        self.list_e.pre = self.list_

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map_:
            node = self._pop(self.map_[key])
            self._push(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map_:
            node = self._pop(self.map_[key])
            node.val = value
        else:
            if len(self.map_) == self.capacity:
                r_node = self._pop_end()
                self.map_.pop(r_node.key)
            node = DListNode(key, value)
            self.map_[key] = node
        self._push(node)

    def _push(self, node):
        node.next = self.list_.next
        node.pre = self.list_
        self.list_.next = node
        node.next.pre = node

    def _pop(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = None
        node.pre = None
        return node

    def _pop_end(self):
        node = self.list_e.pre
        node.pre.next = self.list_e
        self.list_e.pre = node.pre
        node.next = None
        node.pre = None
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.get(1))
# obj.put(3, 3)
# print(obj.get(2))
# obj.put(4, 4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))

