class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        @lru_cache(None)
        def dp(i, mask):
            if i == n:
                return 0
            
            ans = float('inf')
            for j in range(n):
                if not (mask & (1 << j)):
                    ans = min(ans, dp(i+1, mask|1<<j) + (nums1[i] ^ nums2[j]))
            return ans
        
        return dp(0, 0)
        