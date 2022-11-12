class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        start = 0
        g.sort()
        s.sort()
        i = j = ans = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans, i = ans + 1, i + 1
            j += 1
            
        return ans
        