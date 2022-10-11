# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t, h = head, head
        for i in range(n):
            if h:
                h = h.next
            else:
                return None
        
        if not h:
            return t.next
        
        prev = None
        while h and t:
            prev = t
            t = t.next
            h = h.next
        
        prev.next = t.next
        t.next = None
        return head