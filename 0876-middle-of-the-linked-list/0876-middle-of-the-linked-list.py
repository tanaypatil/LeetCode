# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h, t = head, head
        while h:
            h = h.next
            if h:
                h = h.next
            else:
                return t
            t = t.next
        return t
        