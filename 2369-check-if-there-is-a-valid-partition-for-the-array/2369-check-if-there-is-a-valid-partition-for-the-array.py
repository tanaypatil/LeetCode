class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def dp(i):
            if i >= len(nums):
                return True
            if (
                n-i >= 2 and nums[i] == nums[i+1] and dp(i+2)
            ) or (
                n-i >= 3 and (
                    (nums[i] == nums[i+1] == nums[i+2] and dp(i+3)
                    ) or (
                        nums[i] == nums[i+1]-1 and nums[i+1] == nums[i+2]-1 and dp(i+3)
                    )
                )
            ):
                    return True
                
            return False
        
        return dp(0)