from typing import Optional  # ListNode or None


class ListNode:
    def __init__(self, val=0, node=None):
        self.val = val
        self.next = node


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    p1 = l1
    p2 = l2
    flag = 0
    p = head = None
    while p1 and p2:
        x = p1.val + p2.val + flag
        tmp = ListNode(0)
        if p is not None:
            p.next = tmp
        else:
            p = head = tmp
        p = tmp
        p.val = x % 10
        flag = x // 10
        p1 = p1.next
        p2 = p2.next
    while p1:
        x = p1.val + flag
        tmp = ListNode(0)
        p.next = tmp
        p = tmp
        p.val = x % 10
        flag = x // 10
        p1 = p1.next
    while p2:
        x = p2.val + flag
        tmp = ListNode(0)
        p.next = tmp
        p = tmp
        p.val = x % 10
        flag = x // 10
        p2 = p2.next
    if flag:
        tmp = ListNode(0)
        p.next = tmp
        p = tmp
        p.val = flag

    return head