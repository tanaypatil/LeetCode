class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.min_removals = float('inf')
        self.ans = set()
        stack = []
        def dfs(i, path):
            if i >= len(s):
                if not stack:
                    removals = len(s)-len(path)
                    if removals < self.min_removals:
                        self.ans = set()
                        self.ans.add(path)
                    elif removals == self.min_removals:
                        self.ans.add(path)
                    self.min_removals = min(removals, self.min_removals)
                return
            
            if (i, path) in self.mem:
                return
            
            if s[i] == "(":
                stack.append(s[i])
                dfs(i+1, path+s[i])
                stack.pop()
            elif s[i] == ")":
                if stack:
                    c = stack.pop()
                    dfs(i+1, path+s[i])
                    stack.append(c)
            else:
                dfs(i+1, path+s[i])
                return
            
            if i-len(path) < self.min_removals:
                dfs(i+1, path)
                
            self.mem[(i, path)] = True
        
        self.mem = {}
        dfs(0, "")
        return self.ans
                        
            