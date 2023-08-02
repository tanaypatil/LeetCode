class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.min_removals = float('inf')
        self.ans = set()
        
        def dfs(i, path, stack):
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
            
            if s[i] == "(":
                dfs(i+1, path+s[i], stack+[s[i]])
            elif s[i] == ")":
                if stack:
                    stack.pop()
                    dfs(i+1, path+s[i], stack)
                    stack.append("(")
            else:
                dfs(i+1, path+s[i], stack)
                return
            dfs(i+1, path, stack)
        
        dfs(0, "", [])
        return self.ans
                        
            