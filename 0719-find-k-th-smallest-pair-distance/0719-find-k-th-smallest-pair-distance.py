class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def enough(diff):
            i, j, count = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= diff:
                    j += 1
                count += j-i-1
                i += 1
            return count >= k
            
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = left + (right-left) // 2
            if not enough(mid):
                left = mid + 1
            else:
                right = mid
        return left
        