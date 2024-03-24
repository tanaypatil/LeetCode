class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        n = len(nums)
        q, r = divmod(sum(nums), 4)
        nums.sort(reverse=True)
        if r or nums[0] > q: return False
        
        def dp(left_k, mask, curr_sum=0, next_index=0):
            if left_k == 1:
                return True
            
            if curr_sum == q:
                return dp(left_k-1, mask)
            
            for i in range(next_index, n):
                if not (mask & (1<<i)) and nums[i] + curr_sum <= q:
                    if dp(left_k, mask | 1<<i, curr_sum + nums[i], i+1):
                        return True
                    if not curr_sum: break
                    
            return False
        
        return dp(4, 0)
                    