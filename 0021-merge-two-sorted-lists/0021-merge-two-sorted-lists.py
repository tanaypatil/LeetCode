# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tc = ListNode()
        p = tc
        ta, tb = list1, list2
        if ta is None:
            return tb
        if tb is None:
            return ta
        if ta.val <= tb.val:
            tc.val = ta.val
            ta = ta.next
        else:
            tc.val = tb.val
            tb = tb.next
        while ta is not None and tb is not None:
            if ta.val <= tb.val:
                t = ListNode(ta.val)
                ta = ta.next
            else:
                t = ListNode(tb.val)
                tb = tb.next
            tc.next = t
            tc = tc.next
        while ta is not None:
            tc.next = ListNode(ta.val)
            tc = tc.next
            ta = ta.next
        while tb is not None:
            tc.next = ListNode(tb.val)
            tc = tc.next
            tb = tb.next
        return p
                
            