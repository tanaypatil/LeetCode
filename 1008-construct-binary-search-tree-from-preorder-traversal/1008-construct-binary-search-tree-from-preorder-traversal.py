# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        node = TreeNode(preorder[0])
        
        node_val = preorder.pop(0)
        
        i = 0
        while i < len(preorder):
            if preorder[i] > node_val:
                break
            i += 1
        
        node.left = self.bstFromPreorder(preorder[:i])
        node.right = self.bstFromPreorder(preorder[i:])
        
        return node
        