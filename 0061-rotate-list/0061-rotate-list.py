# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        
        l = 0
        t = head
        
        while t:
            l += 1
            t = t.next
            
        t = head
        p = None
        k = k % l
        if not k:
            return head
        for i in range(l-k):
            p = t
            t = t.next
        
        p.next = None
        h = t
        
        while t and t.next:
            t = t.next
        if t:
            t.next = head
        return h
        