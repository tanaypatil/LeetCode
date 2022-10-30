from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        pops = 0
        for i, a in enumerate(num):
            while stack and int(stack[0]) > int(a) and pops < k:
                stack.popleft()
                pops += 1
            stack.appendleft(a)
        
        while stack and pops < k:
            stack.popleft()
            pops += 1
            
        if not stack:
            return "0"
        
        stack.reverse()
        return str(int(''.join(stack)))