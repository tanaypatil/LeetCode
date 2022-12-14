class Solution:
    def dfs(self, index, path):
        if (index >= len(Solution.s)) or (len(path) >= len(Solution.t)):
            return 1 if path == Solution.t else 0
        if len(Solution.s)-index + len(path) < len(Solution.t):
            return 0
        if (index, path) in Solution.mem:
            return Solution.mem[(index, path)]
        taken = 0
        if Solution.s[index] == Solution.t[len(path)]:
            taken += self.dfs(index+1, path+Solution.s[index])
        not_taken =  self.dfs(index+1,  path)
        c = taken + not_taken
        Solution.mem[(index, path)] = c
        return c
           
        
    def numDistinct(self, s: str, t: str) -> int:
        Solution.mem = {}
        Solution.s, Solution.t = s, t
        return self.dfs(0, "")
        