# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a = b = head
        while a and b:
            if a:
                a = a.next
            if b:
                b = b.next
                if b:
                    b = b.next
            if a and b and a == b:
                return True
        return False
        