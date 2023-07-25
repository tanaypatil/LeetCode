# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        t, h = head, head
        while t and h:
            if not h.next.next:
                break
            h = h.next.next
            t = t.next
        f, s = head, t.next
        t.next = None
        
        p = None
        while f:
            n = f.next
            f.next = p
            p = f
            f = n
        f = p
        
        m = float('-inf')
        while s and f:
            m = max(m, s.val+f.val)
            s = s.next
            f = f.next
        return m