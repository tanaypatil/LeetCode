# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self, root, low, high):
        if not root:
            return True
        
        return low < root.val < high and self.isValid(root.left, low, root.val) and self.isValid(root.right, root.val, high)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))