# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isHB(self, root):
        if not root:
            return True, 0
        leftb, lefth = self.isHB(root.left)
        rightb, righth = self.isHB(root.right)
        
        if leftb and rightb and abs(lefth-righth) <= 1:
            return True, max(lefth, righth) + 1
        
        return False, max(lefth, righth) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isHB(root)[0]
        
        