class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(s, stack):
            if len(s) == 2*n:
                if not stack:
                    ans.append(s)
                return
            
            if s.count("(") < n:
                dfs(s + "(", stack + ["("])
            if stack:
                stack.pop()
                dfs(s + ")", stack)

        ans = []
        dfs("", [])
        return ans

        