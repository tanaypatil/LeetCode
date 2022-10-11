# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        first_odd, last_odd = None, None
        first_even, last_even = None, None
        
        curr = head
        c = 1
        while curr:
            if c % 2:
                if not first_odd:
                    first_odd = curr
                if last_odd:
                    last_odd.next = curr
                last_odd = curr
            else:
                if not first_even:
                    first_even = curr
                if last_even:
                    last_even.next = curr
                last_even = curr
            curr = curr.next
            c += 1
        if not last_odd:
            return first_even
        last_odd.next = first_even
        if last_even:
            last_even.next = None
        
        return first_odd
        