# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件
        if not head or not head.next:
            return head
        
        # 分割
        slow,fast = head,head.next
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
        # slow走到mid前 fast走到尾部
        mid,slow.next = slow.next,None
        # 递归获取左右两个
        left,right = self.sortList(head),self.sortList(mid)
        ret=cur = ListNode(0)
        # 开始拼接
        while left and right:
            if left.val < right.val:
                cur.next,left = left,left.next
            else:
                cur.next,right = right,right.next
            # 移动cur
            cur = cur.next
        cur.next = left if left else right
        return ret.next




if __name__ == "__main__":
    s = Solution()
    head = ListNode(4,ListNode(2,ListNode(1,ListNode(3))))
    ret = s.sortList(head)
    while ret:
        print(ret.val,end=" ")
        ret = ret.next