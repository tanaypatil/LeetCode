# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


def vt(root, res, h, b):
    if not root:
        return
    res[h].append((root.val, b))
    if root.left:
        vt(root.left, res, h-1, b+1)
    if root.right:
        vt(root.right, res, h+1, b+1)


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        vt(root, res, 0, 0)
        ret = []
        for k in sorted(res.keys()):
            res[k].sort(key=lambda x: (x[1], x[0]))
            t = [x[0] for x in res[k]]
            ret.append(t)
        return ret