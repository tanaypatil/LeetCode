class Solution:
    def minInsertions(self, s: str) -> int:
        closingPCount = 0
        stack = deque()
        invalid = 0
        for c in s:
            if c == "(":
                if closingPCount == 1:
                    invalid += 1
                    closingPCount = 0
                    if stack:
                        stack.pop()
                    else:
                        invalid += 1
                stack.append(c)
            else:
                if closingPCount == 0:
                    closingPCount += 1
                else:
                    if stack:
                        stack.pop()
                    else:
                        invalid += 1
                    closingPCount = 0
        if closingPCount == 1:
            invalid += 1
            if stack:
                stack.pop()
            else:
                invalid += 1
        return invalid + len(stack)*2
                    
        