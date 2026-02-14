# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t, h = head, head
        while h and t:
            h = h.next
            if h:
                h = h.next
            else:
                return None
            t = t.next
            if h == t:
                break
        s = head
        while s and t and s != t:
            s = s.next
            t = t.next
        return t