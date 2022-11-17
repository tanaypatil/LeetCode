# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if not root:
            return []
        
        res = [root.val]
        q.append(root)
        
        while q:
            s = len(q)
            for i in range(s):
                node = q.popleft()
                
                if node.right:
                    q.append(node.right)
                    
                if node.left:
                    q.append(node.left)
            if q:        
                res.append(q[0].val)
        return res