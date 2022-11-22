# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def iot(root, ret):
    if not root:
        return
    iot(root.left, ret)
    ret.append(root.val)
    iot(root.right, ret)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return -1
        
        ret = []
        iot(root, ret)
        
        return ret[k-1]