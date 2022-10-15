# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getLR(head):
    if not head: return None, None
    if not head.next: return head, None
    t, h = head, head
    prevt = None
    while t and h:
        h = h.next
        if not h: break
        h = h.next
        prevt = t
        t = t.next
    prevt.next = None
    return head, t


def merge(l, r):
    if not l:
        return r
    if not r:
        return l
    cl, cr = l, r
    nc = None
    s = None
    while cl and cr:
        if cl.val <= cr.val:
            n = ListNode(cl.val)
            if not nc:
                nc = n
                s = nc
            else:
                nc.next = n
                nc = nc.next
            cl = cl.next
        else:
            n = ListNode(cr.val)
            if not nc:
                nc = n
                s = nc
            else:
                nc.next = n
                nc = nc.next
            cr = cr.next
    while cl:
        n = ListNode(cl.val)
        nc.next = n
        nc = nc.next
        cl = cl.next
    while cr:
        n = ListNode(cr.val)
        nc.next = n
        nc = nc.next
        cr = cr.next
    # print(s)
    return s


def mergeSort(head):
    # print("head ----> ", head)
    if not head or not head.next:
        return head
    l, r = getLR(head)
    sl = mergeSort(l)
    sr = mergeSort(r)
    # print(sl, "    |||||  ", sr)
    if sl and sr:
        return merge(sl, sr)
    if sl: return sl
    if sr: return sr


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return mergeSort(head)