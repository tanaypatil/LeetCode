class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        cur_min = nums[0]
        
        for k in range(1, len(nums)):
            while stack and stack[-1][0] <= nums[k]:
                stack.pop()
            if stack and stack[-1][1] < nums[k]:
                return True
            stack.append([nums[k], cur_min])
            cur_min = min(cur_min, nums[k])
        return False