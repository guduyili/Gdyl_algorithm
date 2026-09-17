# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 公共交点长度为c
        # A: a-c + c
        # B: b-c + c
        # 先遍历完A再遍历B到交点： a + (b-c) 
        # 先遍历完B再遍历A到交点： b + (a-c)
        # 如果有交点则相等
        #  a + (b-c)  = b + (a-c)
        A = headA
        B = headB

        while A != B:
            # 先遍历完A再遍历B到交点
            A = A.next if A else headB
            # 先遍历完B再遍历A到交点
            B = B.next if B else headA
        return A


if __name__ == "__main__":
    # 创建链表A: 4 -> 1 -> 8 -> 4 -> 5
    headA = ListNode(4)
    headA.next = ListNode(1)
    intersection = ListNode(8)
    headA.next.next = intersection
    intersection.next = ListNode(4)
    intersection.next.next = ListNode(5)

    # 创建链表B: 5 -> 0 -> 1 -> 8 -> 4 -> 5
    headB = ListNode(5)
    headB.next = ListNode(0)
    headB.next.next = ListNode(1)
    headB.next.next.next = intersection

    solution = Solution()
    result = solution.getIntersectionNode(headA, headB)

    if result:
        print(f"Intersection at node with value: {result.val}")
    else:
        print("No intersection.")