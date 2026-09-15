# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sml_dummy  = ListNode(0)
        big_dummy  = ListNode(0)
        sml,big = sml_dummy,big_dummy
        cur  = head
        while cur:
            if cur.val < x:
                sml.next = cur
                sml = sml.next
            else:
                big.next = cur
                big = big.next
            cur = cur.next
        sml.next = big_dummy.next
        big.next = None
        return sml_dummy.next

if __name__ == "__main__":
    s = Solution()
    # 创建一个链表 1 -> 4 -> 3 -> 2 -> 5 -> 2
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    x = 3
    new_head = s.partition(head, x)

    # 输出新的链表
    cur = new_head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")