def genP(n, stack, s, ans, openingPCount):
    if len(s) >= n:
        if not stack:
            ans.append(s)
        return
    if openingPCount < n//2:
        genP(n, stack+["("], s+"(", ans, openingPCount+1)
    p = stack.pop() if stack else None
    if p and p == "(":
        genP(n, stack, s+")", ans, openingPCount)
        
        

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        genP(2*n, [], "", ans, 0)
        return ans