# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        la = lb = 0
        
        ta = headA
        while ta:
            ta = ta.next
            la += 1
        
        tb = headB
        while tb:
            tb = tb.next
            lb += 1
        
        ta, tb = headA, headB
        
        if la > lb:
            for i in range(la-lb):
                ta = ta.next
        else:
            for i in range(lb-la):
                tb = tb.next
        
        while ta and tb:
            if ta == tb:
                return ta
            ta, tb = ta.next, tb.next
            
        return None