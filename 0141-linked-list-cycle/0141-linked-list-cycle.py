# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h, t = head, head
        while h and t:
            t = t.next
            h = h.next
            if h:
                h = h.next
            if h == t and h:
                return True
        return False
        