# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levels = defaultdict(list)
        q = deque({(root, 0, 0)})
        
        while q:
            node, vl, bl = q.popleft()
            levels[vl].append((node.val, bl))
            if node.left:
                q.append((node.left, vl-1, bl+1))
            if node.right:
                q.append((node.right, vl+1, bl+1))
        return [[v for v, b in sorted(levels[vl], key= lambda x: (x[1], x[0]))] for vl in sorted(levels.keys())]
            