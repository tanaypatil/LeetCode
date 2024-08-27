class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = len(set(nums))
        ans = 0
        counts = Counter()
        l = 0
        for r in range(len(nums)):
            counts[nums[r]] += 1
            while len(counts) == total:
                counts[nums[l]] -= 1
                if not counts[nums[l]]:
                    del counts[nums[l]]
                l += 1
            ans += l
            
        return ans
        