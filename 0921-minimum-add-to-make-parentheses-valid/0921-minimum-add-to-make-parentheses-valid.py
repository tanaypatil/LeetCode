class Solution:
    def minAddToMakeValid(self, string: str) -> int:
        stack = deque()
        count = 0
        for c in string:
            if c == "(":
                stack.appendleft(c)
            else:
                if not stack:
                    count += 1
                    continue
                stack.popleft()
        return count if not stack else len(stack) + count