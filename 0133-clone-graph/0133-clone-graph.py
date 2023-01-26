"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return None
            if node in mem:
                return mem[node]
            new_node = Node(node.val)
            mem[node] = new_node
            for neighbor in node.neighbors:
                if neighbor not in mem:
                    new_neighbor = dfs(neighbor)
                    if new_neighbor:
                        new_node.neighbors.append(new_neighbor)
                else:
                    new_node.neighbors.append(mem[neighbor])
            return new_node
        
        mem = {}
        return dfs(node)