# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if root.val == subRoot.val:
            if self.isSame(root, subRoot):
                return True
        
        if self.isSubtree(root.left, subRoot):
            return True
        
        if self.isSubtree(root.right, subRoot):
            return True
        
        return False