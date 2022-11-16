from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        depth = 0
        if root:
            q.append(root)
        else:
            return 0
        while len(q):
            depth += 1
            size = len(q)
            for i in range(size):
                a = q.popleft()
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
        return depth