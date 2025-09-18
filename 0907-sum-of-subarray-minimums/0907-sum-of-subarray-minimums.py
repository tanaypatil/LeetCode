class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        mins = [0]
        stack = [0]
        
        for i in range(1, len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            mins.append((arr[i] * (i-stack[-1])) + mins[stack[-1]])
            stack.append(i)
        return sum(mins)%(10**9+7)
        