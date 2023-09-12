class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        pref_xor = [arr[0]]
        
        ans = 0
        for i in range(1, n):
            pref_xor.append(pref_xor[-1]^arr[i])
            if not pref_xor[-1]:
                ans += i
        
        for i in range(n-1):
            for k in range(i+1, n):
                pref_xor[k] ^= pref_xor[i]
                if not pref_xor[k]:
                    ans += k-i-1
                    
        return ans
                
        
        