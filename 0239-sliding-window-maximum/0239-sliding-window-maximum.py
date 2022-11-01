from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
                
            queue.append(i)
            
            if queue[0] <= i-k:
                queue.popleft()
                
            if i >= k-1 and queue:
                res.append(nums[queue[0]])
                
        return res