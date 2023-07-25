# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = head
        s = None
        p = None
        for i in range(left-1):
            p = l
            l = l.next
        s = p
        p = l
        l = l.next
        for i in range(right-left):
            n = l.next
            l.next = p
            p = l
            l = n
        if not s:
            head.next = l
            return p
        c = s.next
        s.next = p
        c.next = l
        return head