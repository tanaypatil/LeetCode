# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseK(self, head, n, k):
        if not head or not head.next or n < k:
            return head
        t = head
        for i in range(k-1):
            t = t.next
        nex = t.next
        nexl = self.reverseK(nex, n-k, k)
        t.next = None
        
        p = None
        t = head
        
        while t:
            nex = t.next
            t.next = p
            p = t
            t = nex
        
        head.next = nexl
        return p
    
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        t = head
        while t:
            l += 1
            t = t.next
        return self. reverseK(head, l, k)