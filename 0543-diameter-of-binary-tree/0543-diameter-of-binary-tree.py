# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def treeDiam(root, diam):
    if not root:
        return -1
    l = treeDiam(root.left, diam) + 1
    r = treeDiam(root.right, diam) + 1
    diam[0] = max(diam[0], l+r)
    return max(l, r)
    

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = [0]
        treeDiam(root, diam)
        return diam[0]