class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total = 0
        
        for i in range(len(height)):
            while len(stack) > 0 and height[stack[-1]] < height[i]:
                poppedIdx = stack.pop()
                
                if len(stack) == 0:
                    break
                    
                heightVal = min(height[stack[-1]], height[i]) - height[poppedIdx]
                print(heightVal)
                length = i - stack[-1] - 1
                total += heightVal * length
            
            stack.append(i)
        
        return total