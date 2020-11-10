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
        node_map = defaultdict(Node)

        def build(head):
            if not head:
                return None
            head_ = Node(head.val)
            node_map[head] = head_
            next_ = head.next
            if next_:
                if next_ not in node_map:
                    head_.next = build(head.next)
                else:
                    head_.next = node_map[next_]
            random_ = head.random
            if random_:
                if random_ not in node_map:
                    head_.random = build(head.random)
                else:
                    head_.random = node_map[random_]

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
