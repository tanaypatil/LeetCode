class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not k:
            return 0
        ans, l, p = 0, 0, 1
        for r in range(len(nums)):
            p *= nums[r]
            while l <= r and p >= k:
                p //= nums[l]
                l += 1
            ans += r-l+1
        return ans
        