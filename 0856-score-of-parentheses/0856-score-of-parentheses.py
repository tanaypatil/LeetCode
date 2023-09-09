class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = deque()
        score = 1
        ans = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                j = stack.pop()
                if not stack:
                    # print(s, j, i)
                    score *= 2*self.scoreOfParentheses(s[j+1:i])
                    if not score: score = 1
                    ans += score
                    # print(ans)
                    score = 1
        # print(s, ans)
        return ans
                    
        