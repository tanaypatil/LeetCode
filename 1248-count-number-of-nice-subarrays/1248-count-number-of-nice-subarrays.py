from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        s, c = 0, 0
        for i, num in enumerate(nums):
            s += (1 if num & 1 else 0)
            c += freq[s-k]
            freq[s] += 1
        return c