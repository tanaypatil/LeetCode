# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ret = []
    def preOrd(self, root):
        if not root:
            return
        Solution.ret.append(root.val)
        self.preOrd(root.left)
        self.preOrd(root.right)
        
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        Solution.ret = []
        self.preOrd(root)
        return Solution.ret
        