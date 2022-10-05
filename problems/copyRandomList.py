from collections import defaultdict
from tools import *


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    @print_
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        map_ = defaultdict(Node)

        def build(root):
            if not root:
                return None
            head_ = Node(root.val)
            map_[root] = head_
            next_ = root.next
            if next_:
                if next_ not in map_:
                    build(next_)
                head_.next = map_[next_]
            random_ = root.random
            if random_:
                if random_ not in map_:
                    build(random_)
                head_.random = map_[random_]
            return head_
        
        return build(head)

    @print_
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        node_map = defaultdict(Node)

        ret = Node(head.val)
        head_ = ret
        node_map[head] = head_
        while head:
            next_ = head.next
            if next_:
                if next_ not in node_map:
                    node_map[next_] = Node(next_.val)
                head_.next = node_map[next_]
            random_ = head.random
            if random_:
                if random_ not in node_map:
                    node_map[random_] = Node(random_.val)
                head_.random = node_map[random_]

            head_ = head_.next
            head = head.next

        return ret


solution = Solution().copyRandomList

solution("[[7,null],[13,0],[11,4],[10,2],[1,0]]")
