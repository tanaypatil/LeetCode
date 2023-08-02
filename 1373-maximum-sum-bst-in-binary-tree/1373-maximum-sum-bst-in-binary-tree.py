# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return True, 0, float('-inf'), float('inf')
        
        is_left, left_sum, max_left, min_left = self.dfs(root.left)
        is_right, right_sum, max_right, min_right = self.dfs(root.right)
        
        if is_left and is_right and max_left < root.val < min_right:
            self.max_sum = max(self.max_sum, left_sum+root.val+right_sum)
            return True, left_sum+root.val+right_sum, max(max_right, root.val), min(min_left, root.val)
        
        return False, left_sum+root.val+right_sum, max_right, min_left
        
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        self.dfs(root)
        return self.max_sum