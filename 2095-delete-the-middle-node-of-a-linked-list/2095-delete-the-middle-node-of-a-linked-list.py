# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t, h = head, head
        if not head:
            return head
        if not head.next:
            return None
        prev = None
        while t and h:
            h = h.next
            if not h: break
            h = h.next
            prev = t
            t = t.next
        prev.next = t.next
        t.next = None
        return head
        