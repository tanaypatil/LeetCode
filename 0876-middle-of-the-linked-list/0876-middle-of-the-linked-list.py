# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return -1
        if not head.next:
            return head
        s = head
        d = head
        prev = None
        while d:
            prev = s
            s = s.next
            d = d.next
            if d:
                d = d.next
            else:
                return prev
        return s if s else -1
        