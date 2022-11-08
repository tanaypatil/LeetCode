from collections import Counter


class Solution:
    def atMostK(self, nums, K):
        res = 0
        left = 0
        counts = Counter()
        for right, num in enumerate(nums):
            if not counts[num]:
                K -= 1
            counts[num] += 1
            while K < 0:
                counts[nums[left]] -= 1
                if not counts[nums[left]]:
                    K += 1
                left += 1
            res += right-left+1
        return res
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k-1)
        