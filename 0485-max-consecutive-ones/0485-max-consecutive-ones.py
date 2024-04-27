class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, curr_count = 0, 0
        for num in nums:
            curr_count = 1 + curr_count if num else 0
            max_count = max(max_count, curr_count)
        return max_count