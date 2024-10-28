class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        ans = float('inf')
        l = s = 0
        
        for r in range(len(nums)):
            s += nums[r]
            # print(s)
            while s >= k:
                ans = min(ans, r-l+1)
                # print(l, r, s)
                s -= nums[l]
                l += 1
        return 0 if ans == float('inf') else ans