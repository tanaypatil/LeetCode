from collections import deque, defaultdict

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
        
    def morris(self, root):
        if not root:
            return []
        inorder = []
        
        curr = root
        while curr:
            pre = curr.left
            if not pre:
                inorder.append(curr.val)
                curr = curr.right
            else:
                while pre.right and pre.right != curr:
                    pre = pre.right
                if not pre.right:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    inorder.append(curr.val)
                    curr = curr.right
        return inorder

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Solution.arr = []
        # self.iot(root)
        # return Solution.arr
        
        return self.morris(root)
        
        if not root:
            return []
        
        res = []
        stack = deque()
        stack.append(root)
        vis = defaultdict(bool)
        while stack:
            r = stack.pop()
            if vis[r]:
                res.append(r.val)
            else:
                if r.right:
                    stack.append(r.right)
                stack.append(r)
                if r.left:
                    stack.append(r.left)
                vis[r] = True
        return res
            