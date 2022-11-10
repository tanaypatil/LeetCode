# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappop



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next
        if not nums:
            return None
        heapify(nums)
        head = ListNode(heappop(nums))
        h = head
        while nums:
            n = ListNode(heappop(nums))
            h.next = n
            h = h.next
        return head