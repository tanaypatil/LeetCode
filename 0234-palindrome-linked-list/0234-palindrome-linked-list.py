# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        prev = None
        h, t = head, head
        odd = 0
        while h and t:
            h = h.next
            if h:
                h = h.next
            else:
                odd = 1
                break
            if not h:
                odd = 0
            nex = t.next
            t.next = prev
            prev = t
            t = nex
            nex = t.next

        if odd:
            f = prev
            s = nex
        else:
            f = prev
            s = t
        
        while f and s:
            if s.val == f.val:
                s = s.next
                f = f.next
            else:
                return False
        return True