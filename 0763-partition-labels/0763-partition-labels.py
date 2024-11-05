class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
            
        l = j = 0
        ans = []
        for i in range(len(s)):
            l = max(l, last[s[i]])
            if i >= l:
                ans.append(i-j+1)
                j = i+1
            
        return ans
        