# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict
    
    
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root or not target:
            return []
        if not k:
            return [target.val]
        
        q = deque()
        parentMap = {}
        q.append(root)
        while q:
            node = q.popleft()
            if node.left:
                parentMap[node.left] = node
                q.append(node.left)
            if node.right:
                parentMap[node.right] = node
                q.append(node.right)
        
        lvl = 0
        
        q = deque()
        q.append((target, 0))
        res = []
        visited = defaultdict(bool)
        while q:
            node, l = q.popleft()
            if not visited[node]:
                visited[node] = True
                if l == k:
                    res.append(node.val)
                if node.left:
                    q.append((node.left, l+1))
                if node.right:
                    q.append((node.right, l+1))
                if node in parentMap:
                    q.append((parentMap[node], l+1))
        return res
            