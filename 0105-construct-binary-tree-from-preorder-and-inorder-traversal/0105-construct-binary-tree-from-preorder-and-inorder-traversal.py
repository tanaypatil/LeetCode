# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        node = TreeNode(preorder[0])
        index = inorder.index(preorder.pop(0))
        node.left = self.buildTree(preorder, inorder[:index])
        node.right = self.buildTree(preorder, inorder[index+1:])
        
        return node