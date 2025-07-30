# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return float('-inf')
            left, right = dfs(root.left), dfs(root.right)
            ans[0] = max(ans[0], root.val + left + right, root.val + max(left, right, 0))
            return root.val + max(left, right, 0)
        ans = [float('-inf')]
        dfs(root)
        return ans[0] if ans[0] != float('-inf') else 0

        