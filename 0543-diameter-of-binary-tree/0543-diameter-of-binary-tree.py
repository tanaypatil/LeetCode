# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            ans[0] = max(ans[0], 1 + left + right)
            return max(left, right) + 1
        ans = [0]
        dfs(root)
        return ans[0]-1
        