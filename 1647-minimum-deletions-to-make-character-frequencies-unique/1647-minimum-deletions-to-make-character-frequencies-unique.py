class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
        
        arr = sorted(counts.values())
        exists = defaultdict(bool)
        for a in arr:
            exists[a] = True
        # print(arr)
        # print(exists)
        
        i = 0
        ans = 0
        while i < len(arr)-1:
            j = i+1
            while j < len(arr) and arr[j] == arr[i]:
                for k in range(arr[j]-1, -1, -1):
                    if not exists[k]:
                        ans += arr[j]-k
                        if k:
                            exists[k] = True
                        break
                j += 1
            i = j
        return ans
        