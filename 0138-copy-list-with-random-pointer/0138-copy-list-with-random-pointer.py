"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class UNode:
    def __init__(self, node):
        self.node = node
        self.copy = None
        self.next = None

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        uhead = UNode(head)
        uh = uhead
        t = head.next
        parent = {head: uhead}
        while t:
            uh.next = UNode(t)
            uh = uh.next
            parent[t] = uh
            t = t.next
        
        copied = Node(head.val)
        c = copied
        t = uhead.next
        uhead.copy = copied
        while t:
            c.next = Node(t.node.val)
            c = c.next
            t.copy = c
            t = t.next
            
        uh = uhead
        
        while uh:
            if uh.node.random:
                uh.copy.random = parent[uh.node.random].copy
            uh = uh.next
        
        return copied
            
        
        