class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        
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
                # print(couple)
                new_nums = nums[:]
                new_nums = new_nums[:couple[0][0]] + new_nums[couple[0][0]+1:]
                if couple[0][0] > couple[1][0]:
                    new_nums = new_nums[:couple[1][0]] + new_nums[couple[1][0]+1:]
                else:
                    new_nums = new_nums[:couple[1][0]-1] + new_nums[couple[1][0]:]
                # print(new_nums)
                ans  = max(ans, i * gcd(couple[0][1], couple[1][1]) + dp(i+1, tuple(new_nums)))
                
            return ans
        
        return dp(1, tuple(nums))
        
            
            
                           