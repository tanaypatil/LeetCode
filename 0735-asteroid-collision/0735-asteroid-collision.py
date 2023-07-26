class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()
                if stack:
                    if stack[-1] > abs(a):
                        continue
                    elif stack[-1] == abs(a):
                        stack.pop()
                    else:
                        stack.append(a)
                else:
                    stack.append(a)
            else:
                stack.append(a)
        return stack
        