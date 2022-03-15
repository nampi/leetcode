from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # next встроенная функция
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    p1 = l1
    p2 = l2
    flag = 0
    head = None
    while p1 and p2:
        x = p1.val + p2.val + flag
        if not head:
            head = ListNode(0)
            p = head
        else:
            tmp = ListNode(0)
            # pycharm тут ругается что к p может быть обращение до объявления, сейчас у тебя правильно срабатывает
            # но на мой взгляд в продуктовом коде лучше объявить до ветвления на случай если вдруг head станен не None
            p.next = tmp
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
