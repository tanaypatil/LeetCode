# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def iot(root, c, k):
    if not root:
        return -1
    
    
    l = iot(root.left, c, k)
    if l != -1:
        return l
    
    c[0] += 1
    if c[0] == k:
        return root.val
    
    r = iot(root.right, c, k)
    if r != -1:
        return r
    return -1


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return iot(root, [0], k)