class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or Counter(s) != Counter(goal):
            return False
        if s == goal: return True
        for i in range(len(goal)-1, -1, -1):
            if goal[i:]+goal[:i] == s:
                return True
        return False