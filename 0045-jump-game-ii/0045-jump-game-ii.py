class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = nums[0]
        jumps = 1
        end = nums[0]
        
        if len(nums) <= 1: return 0
        
        for i in range(1, len(nums)-1):
            max_reach = max(max_reach, i+nums[i])
            if i == end:
                end = max_reach
                jumps += 1
        return jumps
        