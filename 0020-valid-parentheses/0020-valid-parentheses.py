from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if (c == ")" and t != "(") or (c == "}" and t != "{") or (c == "]" and t != "["):
                    return False
        if len(stack) == 0:
            return True
        return False
                