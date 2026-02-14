class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dfs(i, s, path):
            if i > 9:
                if s == n and len(path) == k:
                    ans.add(path)
                return

            if i + s <= n and len(path) + 1 <= k:
                dfs(i+1, s+i, tuple(list(path)+[i]))
            dfs(i+1, s, path)
        
        ans = set()
        dfs(1, 0, tuple())
        return list(ans)