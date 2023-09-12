class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref_xor = [0]*len(arr)
        pref_xor[0] = arr[0]
        
        for i in range(1, len(arr)):
            pref_xor[i] = pref_xor[i-1] ^ arr[i]
        
        res = []
        for l, r in queries:
            if not l: 
                res.append(pref_xor[r])
            else:
                res.append(pref_xor[r]^pref_xor[l-1])
        return res
            
        