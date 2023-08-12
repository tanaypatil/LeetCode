class Solution:
    def validArrangement(self, pairs):
        adj = defaultdict(list)
        deg = Counter()
        for u, v in pairs:
            adj[u].append(v)
            deg[u] += 1
            deg[v] -= 1
        
        for start in adj:
            if deg[start] == 1:
                break

        ans = []
        def dfs(node):
            while adj[node]:
                dfs(nei := adj[node].pop())
                ans.append([node, nei])
        dfs(start)
        return ans[::-1]