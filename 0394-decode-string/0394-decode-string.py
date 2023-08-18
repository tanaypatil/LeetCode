class Solution:
    @lru_cache(None)
    def decodeString(self, s: str) -> str:
        ans = ""
        if not s: return ans
        i = 0
        d = ""
        for i, c in enumerate(s):
            if not c.isnumeric():
                ans += c
            else:
                j = i
                while s[j].isnumeric():
                    d += s[j]
                    j += 1
                i = j-1
                break
        d = int(d) if d else 1
        if i == len(s) - 1: return ans
        stack = deque()
        stack.append(s[i+1])
        i += 2
        r = "["
        while stack and i < len(s):
            if s[i] == "[":
                stack.append("[")
            elif s[i] == "]":
                stack.pop()
            r += s[i]
            i += 1
        ans += self.decodeString(r[1:-1])*d
        ans += self.decodeString(s[i:])
        return ans
        