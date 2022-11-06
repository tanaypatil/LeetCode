from collections import Counter


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count = 0
        start, end = 0, 0
        n = len(nums)
        counts = Counter(nums)
        zero_count = 0

        if counts[0] <= k:
            return n
        
        while start < n and end < n:
            while end < n and (nums[end] == 1 or zero_count < k):
                if not nums[end]: zero_count += 1
                f = 1
                end += 1
            max_count = max(max_count, end-start)
            while start < end and zero_count >= k:
                if not nums[start]: zero_count -= 1
                start += 1
            if start == end:
                start += 1
                end += 1
        return max_count