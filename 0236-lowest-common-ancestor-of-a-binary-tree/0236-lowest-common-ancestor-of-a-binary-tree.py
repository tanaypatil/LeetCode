# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        def dfs(node):
            if not node:
                return False, False
            
            leftp, leftq = dfs(node.left)
            rightp, rightq = dfs(node.right)
            
            foundp, foundq = leftp or rightp or node.val == p.val, leftq or rightq or node.val == q.val
            
            if not self.lca and foundp and foundq:
                self.lca = node
                
            return foundp, foundq
        dfs(root)
        return self.lca
            