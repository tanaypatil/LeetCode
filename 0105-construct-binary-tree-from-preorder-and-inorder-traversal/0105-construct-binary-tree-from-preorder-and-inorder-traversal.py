# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def build(pre, ino):
    if not pre or not ino:
        return None
    # print(pre, ino)
    node = TreeNode(pre[0])
    i = ino.index(pre[0])
    pre.pop(0)
    node.left = build(pre, ino[:i])
    node.right = build(pre, ino[i+1:])
    
    return node



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return build(preorder, inorder)