# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h, t = head, head
        l = 0
        while h and t:
            t = t.next
            h = h.next
            if h:
                h = h.next
            if h == t and h:
                l = 1
                break
        if not l:
            return None
        curr = head
        while curr != t:
            curr = curr.next
            t = t.next
        return curr
            
        