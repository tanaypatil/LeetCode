class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = l = ans = 0
        for r in range(len(nums)):
            if not nums[r]:
                zeroes += 1
            while zeroes > k:
                if not nums[l]:
                    zeroes -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans
        