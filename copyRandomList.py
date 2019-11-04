# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

import collections

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        ref_map = collections.defaultdict(Node)
        new_head = current = Node(head.val, None, None)
        ref_map[head] = new_head
        # check whether the current head is in the ref_map
        while head:
            # check current head has random and is in the ref_map
            if head.random:
                if head.random not in ref_map:
                    ref_map[head.random] = Node(head.random.val, None, None)
                # add random ref to the new list
                current.random = ref_map[head.random]
            # check current head has next and is in the ref_map
            if head.next:
                if head.next not in ref_map:
                    ref_map[head.next] = Node(head.next.val, None, None)
                # add next ref to the new list
                current.next = ref_map[head.next]
            current = current.next
            head = head.next
        return new_head
