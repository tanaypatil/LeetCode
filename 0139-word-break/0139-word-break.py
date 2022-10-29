from collections import Counter, defaultdict


class Solution:
    def find(self, s, wordDict, memo):
        if not s:
            return True
        if s in memo and not memo[s]: return False
        for word in wordDict:
            if s[0] == word[0] and len(s) >= len(word) and s[:len(word)] == word:
                if self.find(s[len(word):], wordDict, memo):
                    return True
        memo[s] = False
        return False
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        counts = Counter(s)
        word_counts = defaultdict(int)
        for word in wordDict:
            c = Counter(word)
            for l in word:
                word_counts[l] += 1
        
        # print(counts)
        # print(word_counts)
        for k, v in counts.items():
            if not word_counts[k]:
                return False
        return self.find(s, wordDict, {})