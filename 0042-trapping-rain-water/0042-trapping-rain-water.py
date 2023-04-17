class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total = 0
        
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                index = stack.pop()
                
                if not stack:
                    break
                    
                ch = min(h, height[stack[-1]])-height[index]
                length = i-stack[-1]-1
                total += ch * length
                
            stack.append(i)
        return total
                