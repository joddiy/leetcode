class Node:
    def __init__(self, k, x, next=None, pre=None):
        self.key = k
        self.val = x
        self.next = next
        self.pre = pre


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}
        self.tail = Node(None, None)
        self.head = Node(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            node = self.map[key]
            self.put(node.key, node.value)
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if exist, remove then add
        if key in self.map:
            self._del(key)
        # if full, remove from end
        elif len(self.map) == self.capacity:
            self._del(self.tail.pre.key)
        node = Node(key, value)
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node
        node.next.pre = node
        self.map[key] = node

    def _del(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.map:
            node = self.map[key]
            node.pre.next = node.next
            node.next.pre = node.pre
            del self.map[key], node
