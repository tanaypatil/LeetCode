# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    arr = []
    
    def iot(self, root):
        if root is None:
            return
        self.iot(root.left)
        Solution.arr.append(root.val)
        self.iot(root.right)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        Solution.arr = []
        self.iot(root)
        return Solution.arr