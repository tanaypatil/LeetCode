# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, m, ans):
            if not root:
                return
            if root.val >= m:
                m = root.val
                ans[0] += 1
            dfs(root.left, m, ans)
            dfs(root.right, m, ans)
        ans = [0]
        dfs(root, float('-inf'), ans)
        return ans[0]
        