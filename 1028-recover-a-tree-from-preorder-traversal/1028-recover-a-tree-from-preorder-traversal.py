# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_left_and_right(self, s, count):
        i = 0
        while i < len(s):
            if s[i] == "-" and s[i-1].isdigit():
                j = i+1
                while j < len(s) and s[j] == "-":
                    j += 1
                if j-i == count:
                    return s[:i], s[j:]
            i += 1
        return s[:i], s[i+count:]
    
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if not traversal: return None
        node_val = ""
        while traversal and traversal[0].isdigit():
            node_val += traversal[0]
            traversal = traversal[1:]
        node = TreeNode(int(node_val))
        dash_count = 0
        while traversal and traversal[0] == "-":
            dash_count += 1
            traversal = traversal[1:]
        left_t, right_t = self.get_left_and_right(traversal, dash_count)
        node.left = self.recoverFromPreorder(left_t)
        node.right = self.recoverFromPreorder(right_t)
        return node
        
        