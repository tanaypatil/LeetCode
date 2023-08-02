class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        final = list(s)
        for i, c in enumerate(s):
            if c == "(":
                stack.append((i, c))
                final[i] = "*"
            elif c == ")":
                if not stack:
                    final[i] = "*"
                else:
                    i, c = stack.pop()
                    final[i] = c
                    
        # while stack:
        #     i, c = stack.pop()
        #     final[i] = "*"
        
        ans = ""
        for f in final:
            if f != "*":
                ans += f
        return ans