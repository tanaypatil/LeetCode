# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def symTree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.val == root2.val and symTree(root1.left, root2.right) and symTree(root1.right, root2.left)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return symTree(root.left, root.right)