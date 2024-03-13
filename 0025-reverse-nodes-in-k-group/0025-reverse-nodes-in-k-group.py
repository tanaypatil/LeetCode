# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        c = 0
        p = head
        while p and c < k:
            p = p.next
            c += 1
            
        if c != k: return head
        
        prev, t, nex = None, head, None
        
        while c and t:
            nex = t.next
            t.next = prev
            prev = t
            t = nex
            c -= 1
        
        if nex:
            head.next = self.reverseKGroup(nex, k)
            
        return prev