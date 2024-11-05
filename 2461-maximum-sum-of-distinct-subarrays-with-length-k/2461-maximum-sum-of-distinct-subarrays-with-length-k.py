class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = Counter()
        s = l = ans = 0
        
        for r in range(len(nums)):
            counts[nums[r]] += 1
            s += nums[r]
            
            while counts[nums[r]] > 1 or r-l+1 > k:
                counts[nums[l]] -= 1
                s -= nums[l]
                l += 1
            
            if r-l+1 == k:
                # print(l, r, s)
                ans = max(ans, s)
        return ans
            