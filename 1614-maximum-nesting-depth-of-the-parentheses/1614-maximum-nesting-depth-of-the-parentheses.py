class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        stack = deque()
        for c in s:
            if c == "(":
                stack.appendleft(c)
            elif c == ")":
                stack.popleft()
            m = max(m, len(stack))
        return m