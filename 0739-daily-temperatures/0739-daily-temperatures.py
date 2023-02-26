from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = deque({n-1})
        for i in range(n-2, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            j = stack[-1] if stack else i
            result[i] = j-i
            stack.append(i)
        return result