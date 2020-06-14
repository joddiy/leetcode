def solution(head):
    p = head
    q = head
    t = head
    while p and q and p.next and q.next and q.next.next:
        p = p.next.next
        q = q.next
        if q == p:
            while q != t:
                q = q.next
                t = t.next
            return t
    return None
