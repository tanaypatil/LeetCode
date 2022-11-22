# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        if not root.right and not root.left:
            return root
        curr = root
        right = curr.right
        curr.right = self.flatten(curr.left)
        curr.left = None
        
        temp = curr
        while temp.right:
            temp = temp.right
            
        temp.right = self.flatten(right)
        
        return curr
        