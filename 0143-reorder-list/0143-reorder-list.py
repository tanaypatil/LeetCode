# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, root: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head = root
        if not head:
            return head
        n = 0
        while head:
            n += 1
            head = head.next
            
        n = (n//2) + 1 if n & 1 else n//2
        c = 0
        head = root
        prev = None
        while head:
            c += 1
            prev = head
            head = head.next
            if c == n:
                break
        if prev:
            prev.next = None
            
        prev = None
        while head:
            nex = head.next
            head.next = prev
            prev = head
            head = nex
        
        temp = root
        head = prev
        while temp and head:
            nex = temp.next
            hnex = head.next
            temp.next = head
            head.next = nex
            
            temp, head = nex, hnex
            
            
            
            
        