from collections import deque


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = deque()
        
        for i in range(n-1, -1, -1):
            while stack and stack[0] <= nums[i]:
                stack.popleft()
            stack.appendleft(nums[i])
            
        ans = [-1]*n
        
        for i in range(n-1, -1, -1):
            while stack and stack[0] <= nums[i]:
                stack.popleft()
            ans[i] = -1 if not stack else stack[0]
            stack.appendleft(nums[i])
            
        return ans