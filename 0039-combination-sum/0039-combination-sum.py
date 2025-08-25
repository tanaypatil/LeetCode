class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i, s, path):
            if i >= len(candidates):
                if s == target:
                    res.add(tuple(path))
                return
            
            if s + candidates[i] <= target:
                dfs(i+1, s+candidates[i], path+[candidates[i]])
                dfs(i, s+candidates[i], path+[candidates[i]])
            
            dfs(i+1, s, path)
            
        res = set()
        dfs(0, 0, [])
        return list(map(list, res))