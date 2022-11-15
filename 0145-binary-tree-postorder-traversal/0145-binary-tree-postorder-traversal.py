# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ret = []
    
    def pot(self, root):
        if not root:
            return
        self.pot(root.left)
        self.pot(root.right)
        Solution.ret.append(root.val)
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        Solution.ret = []
        self.pot(root)
        return Solution.ret