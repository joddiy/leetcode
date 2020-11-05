def solution(head):
    p = head
    q = head
    while p and q and p.next and q.next and q.next.next:
        p = p.next.next
        q = q.next
        if q == p:
            return True
    return False