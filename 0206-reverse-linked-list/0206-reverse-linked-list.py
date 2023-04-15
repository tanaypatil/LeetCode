# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        prev = None
        while h:
            n = h.next
            h.next = prev
            prev = h
            h = n
        return prev