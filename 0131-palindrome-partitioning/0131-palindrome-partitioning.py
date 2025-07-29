class Solution:
    @lru_cache
    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        ret = []
        for i, c in enumerate(s):
            if s[:i+1] == s[:i+1][::-1]:
                for suf in self.partition(s[i+1:]):  # process suffix recursively
                    ret.append([s[:i+1]] + suf)
        return ret