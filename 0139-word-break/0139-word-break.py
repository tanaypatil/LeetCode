from collections import Counter, defaultdict


class Solution:
    def find(self, i):
        if i >= len(Solution.s):
            return True
        if i in Solution.mem:
            return Solution.mem[i]
        for word in Solution.wordDict:
            if Solution.s[i] == word[0] and word == Solution.s[i:i+len(word)]:
                if self.find(i+len(word)):
                    return True
        Solution.mem[i] = False
        return False
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        Solution.s = s
        Solution.wordDict = wordDict
        Solution.mem = {}
        return self.find(0)
        
        