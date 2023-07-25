# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        t = head
        x = head
        l = 0
        while x:
            l += 1
            x = x.next
        if k > l:
            return head
        for i in range(k-1):
            t = t.next
        nex = t.next
        nexl = self.reverseKGroup(nex, k)
        t.next = None
        
        s = head
        p = None
        t = head
        
        while t:
            nex = t.next
            t.next = p
            p = t
            t = nex
        
        head.next = nexl
        return p