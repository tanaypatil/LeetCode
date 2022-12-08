class Solution:
    def find(self, x):
        parent = Solution.parent
        while Solution.parent[x] != x:
            x = Solution.parent[x]
        return x
    
    def union(self, x, y):
        parent = Solution.parent
        rank = Solution.rank
        parentX = self.find(x)
        parentY = self.find(y)
        
        if parentX == parentY:
            return
        
        if rank[parentX] <= rank[parentY]:
            parent[parentX] = parentY
            rank[parentY] += 1
        else:
            parent[parentY] = parentX
            rank[parentX] += 1

    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        Solution.parent = [i for i in range(n)]
        Solution.rank = [0]*n
        
        for i in range(n-1):
            for j in range(i+1, n):
                if self.find(i) != self.find(j):
                    if accounts[i][0] == accounts[j][0] and set(accounts[i][1:]).intersection(set(accounts[j][1:])):
                        self.union(i, j)
                        
        # print(Solution.parent)
        ret = defaultdict(list)
        
        for i in range(n):
            p = self.find(i)
            ret[p] += list(accounts[i][1:])
            
        # print(ret)
            
        res = []
        
        for k, v in ret.items():
            t = []
            name = accounts[k][0]
            emails = list(sorted(list(set(v))))
            t.append(name)
            t += emails
            res.append(t)
        
        return res
        
                