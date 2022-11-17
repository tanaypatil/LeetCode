from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if not root:
            return []
        
        q.append(root)
        c = 0
        res = []
        while q:
            s = len(q)
            c += 1
            tq = deque()
            t = []
            for i in range(s):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    tq.append(node.left)
                if node.right:
                    tq.append(node.right)
            q += tq
            if c & 1:
                res.append(t)
            else:
                res.append(t[::-1])
        
        return res
        