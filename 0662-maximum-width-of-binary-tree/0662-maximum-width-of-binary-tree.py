# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ret = 1
        
        q = deque()
        q.append((root, 1))
        
        while q:
            s = len(q)
            ret = max(ret, q[-1][1]-q[0][1]+1)
            for _ in range(s):
                node, num = q.popleft()
                if node.left:
                    q.append((node.left, 2*num))
                if node.right:
                    q.append((node.right, 2*num+1))
        return ret