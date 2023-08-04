class Solution:
    def canPartitionKSubsets(self, nums, k):
        n = len(nums)
        q, r = divmod(sum(nums), k)
        nums.sort(reverse=True)
        if r or nums[0] > q: return False
        mem = defaultdict(bool)
        
        def dp(rest_k, mask, cur_sum = 0, next_index = 0):
            if rest_k == 1:
                return True
            
            if cur_sum == q:
                return dp(rest_k-1, mask)
            
            if mask in mem:
                return mem[mask]
            
            for i in range(next_index, n):
                if not (mask & (1 << i)) and nums[i] + cur_sum <= q:
                    if dp(rest_k, mask | (1 << i), nums[i] + cur_sum, i+1):
                        mem[mask] = True
                        return True
                    if cur_sum == 0:
                        break
            return False
        
        return dp(k, 0)