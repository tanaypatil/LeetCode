# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        q = deque({root})
        s = None
        while q:
            node = q.popleft()
            if node.val == start:
                s = node
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)
                
        q = deque({s})
        t = -1
        visited = defaultdict(bool)
        while q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                visited[node.val] = True
                if node.left and not visited[node.left.val]:
                    q.append(node.left)
                if node.right and not visited[node.right.val]:
                    q.append(node.right)
                if node in parent and not visited[parent[node].val]:
                    q.append(parent[node])
            t += 1
        return t
        