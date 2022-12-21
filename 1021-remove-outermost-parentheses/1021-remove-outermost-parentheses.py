class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = deque()
        res = ""
        last = 0
        
        for i, c in enumerate(s):
            if c == "(":
                stack.appendleft("(")
            else:
                stack.popleft()
            if not stack:
                res += s[last+1:i]
                last = i+1
        return res
        
        