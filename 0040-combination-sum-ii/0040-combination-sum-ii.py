class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        @lru_cache
        def dfs(i, s, path):
            if i >= len(candidates):
                if s == target:
                    l = path.strip().split(",")
                    res.add(tuple(map(int, [x for x in l if x != ''])))
                return

            if s + candidates[i] <= target:
                dfs(i+1, s+candidates[i], path + "," + str(candidates[i]))
            dfs(i+1, s, path)

        res = set()
        candidates.sort()
        dfs(0, 0, "")
        return list(res)
        