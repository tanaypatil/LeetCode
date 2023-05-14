# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def lca(root, p, q, res):
    if not root:
        return False
    
    left, right = lca(root.left, p, q, res), lca(root.right, p, q, res)
    
    if left and right and not res[0]:
        res[0] = root
        return True
    
    if (left or right) and (root.val == p.val or root.val == q.val) and not res[0]:
        res[0] = root
        return True
    
    if root.val == p.val or root.val == q.val:
        return True
    
    return left or right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [None]
        lca(root, p, q, res)
        return res[0]