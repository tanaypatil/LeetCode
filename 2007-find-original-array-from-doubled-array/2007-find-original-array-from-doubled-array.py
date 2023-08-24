class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        if len(changed) & 1:
            return []
        counts = Counter(changed)
        
        ans = []
        for num in changed:
            if counts[num]:
                counts[num] -= 1
                if counts[2*num]:
                    counts[2*num] -= 1
                    ans.append(num)
                
        if len(ans) != len(changed) // 2:
            return []
        
        return ans
        
        