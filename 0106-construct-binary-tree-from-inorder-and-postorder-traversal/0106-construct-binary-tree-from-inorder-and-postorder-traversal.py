# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        node = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        postorder.pop()
        node.right = self.buildTree(inorder[i+1:], postorder)
        node.left = self.buildTree(inorder[:i], postorder)

        return node