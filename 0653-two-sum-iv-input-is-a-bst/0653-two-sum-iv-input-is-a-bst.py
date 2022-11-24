# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hm = {}
    s = 0
    def find(self, root):
        if not root: return
        if Solution.s-root.val in Solution.hm:
            return True
        Solution.hm[root.val] = 1
        return self.find(root.left) or self.find(root.right)
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        Solution.hm = {}
        Solution.s = k
        return self.find(root)
        