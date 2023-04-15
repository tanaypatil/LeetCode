# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t, h = head, head
        while t and h:
            t = t.next
            h = h.next
            if h:
                h = h.next
                if t == h:
                    return True
        return False
        