class Solution:
    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        ans = []
        def dp(s, path):
            if not s:
                ans.append(' '.join(path))
                return
            for word in words:
                if len(word) <= len(s) and s[:len(word)] == word:
                    dp(s[len(word):], path+[word])
        dp(s, [])
        return ans
                