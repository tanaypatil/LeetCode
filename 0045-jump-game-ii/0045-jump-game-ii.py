from collections import deque, defaultdict


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_reach = nums[0]
        end = nums[0]
        
        jumps = 1
        
        if n <= 1:
            return 0
        
        for i in range(1, n-1):
            max_reach = max(i + nums[i], max_reach)
            if i == end:
                end = max_reach
                jumps += 1
        return jumps