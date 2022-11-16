# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def mps(root, m):
    if not root:
        return 'r'
    left = mps(root.left, m)
    right = mps(root.right, m)
    
    m[0] = max(m[0], -9999999999 if left == 'r' else left, -99999999 if right=='r' else right, max(0 if left=='r' else left, 0 if right=='r' else right)+root.val, (0 if left=='r' else left)+(0 if right=='r' else right)+root.val, root.val)
    
    return max(max((0 if left=='r' else left), (0 if right=='r' else right)) + root.val, root.val)


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = [-999999999999]
        mps(root, m)
        return m[0]
        