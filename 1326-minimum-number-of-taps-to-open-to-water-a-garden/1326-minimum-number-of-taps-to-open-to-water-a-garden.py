class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0] * (n + 1)
        
        for i, r in enumerate(ranges):
            left, right = max(0, i - r), min(n, i + r)
            max_range[left] = max(max_range[left], right - left)
            
        def jump(nums: List[int]) -> int:
            max_reach = nums[0]
            jumps = 1
            end = nums[0]

            if len(nums) <= 1: return 0

            for i in range(1, len(nums)-1):
                max_reach = max(max_reach, i+nums[i])
                if i == end:
                    end = max_reach
                    jumps += 1
            return jumps if end >= len(nums)-1 else -1
        
        return jump(max_range)