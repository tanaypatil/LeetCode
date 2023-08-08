class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def gcd(a, b):
            if b > a:
                return gcd(b, a)
            
            if b == 0:
                return a
            
            return gcd(b, a % b)
        
        @lru_cache(None)
        def dp(i, nums):
            if i >= (n // 2) + 1:
                return 0
            
            ans = float('-inf')
            for couple in combinations(list(enumerate(nums)), 2):
                new_nums = list(nums[:])
                new_nums.pop(couple[0][0])
                new_nums.pop(couple[1][0] if couple[0][0] > couple[1][0] else couple[1][0]-1)
                # if couple[0][0] > couple[1][0]:
                #     new_nums.pop(couple[1][0])
                # else:
                #     new_nums.pop(couple[1][0]-1)
                ans  = max(ans, i * gcd(couple[0][1], couple[1][1]) + dp(i+1, tuple(new_nums)))
                
            return ans
        
        return dp(1, tuple(nums))
        
            
            
                           