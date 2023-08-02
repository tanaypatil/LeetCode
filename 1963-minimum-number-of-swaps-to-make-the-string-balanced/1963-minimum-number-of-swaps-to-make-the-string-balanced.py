class Solution:
    def minSwaps(self, s: str) -> int:
        stack = deque()
        replaceable = 0
        for c in s:
            if c == "[":
                stack.append(c)
            else:
                if not stack:
                    replaceable += 1
                else:
                    stack.pop()
        return (replaceable + 1) // 2