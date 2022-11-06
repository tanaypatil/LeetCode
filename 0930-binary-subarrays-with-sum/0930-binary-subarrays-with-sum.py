from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1
        for num in nums:
            s += num
            count += freq[s-goal]
            freq[s] += 1
        return count