class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        q = deque()
        revGraph = defaultdict(list)
        inDegree = defaultdict(int)
        
        for i, adj_nodes in enumerate(graph):
            for node in adj_nodes:
                revGraph[node].append(i)
                inDegree[i] += 1
            if not adj_nodes:
                q.append(i)
                
        ret = []
        while q:
            node = q.popleft()
            ret.append(node)
            for i in revGraph[node]:
                inDegree[i] -= 1
                if not inDegree[i]:
                    q.append(i)
                    
        return sorted(ret)
        
        
                
                    
        