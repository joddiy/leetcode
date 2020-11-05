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
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node) 
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            self._remove(self.dict[key])
        node = Node(key, value)
        self._add(node)
        self.dict[key] = node
        while len(self.dict) > self.capacity:
            tmp_node = self.head.next
            self._remove(tmp_node)
            del self.dict[tmp_node.key]

    def _remove(self, node):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p
    
    def _add(self, node):
        p = self.tail.pre
        p.next = node
        node.pre = p
        node.next = self.tail
        self.tail.pre = node