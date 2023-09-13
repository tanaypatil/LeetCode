class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        uf = UnionFind(n)
        seen = {}
        for i, word in enumerate(words): 
            m = reduce(or_, (1<<ord(ch)-97 for ch in word))
            if m in seen: uf.union(i, seen[m])
            for k in range(26): 
                if m ^ 1<<k in seen: uf.union(i, seen[m ^ 1<<k])
                if m & 1<<k: 
                    mm = m ^ 1<<k ^ 1<<26
                    if mm in seen: uf.union(i, seen[mm])
                    seen[mm] = i
            seen[m] = i 
        freq = Counter(uf.find(i) for i in range(n))
        return [len(freq), max(freq.values())]
                        
        
        
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1
        