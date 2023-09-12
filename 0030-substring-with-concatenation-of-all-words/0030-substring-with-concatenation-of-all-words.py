class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        S: int = len(s)
        W: int = len(words)
        L: int = len(words[0])

        wordCounts: Dict[str, int] = defaultdict(int)
        for word in words:
            wordCounts[word] += 1

        def concatStartsAt(concatStart: int) -> bool:
            wordCountsCopy: Dict[str, int] = wordCounts.copy()

            for iW in range(W):
                wordStart: int = concatStart + iW * L
                word: str = s[wordStart : wordStart + L]

                if not wordCountsCopy[word]:
                    return False
                wordCountsCopy[word] -= 1

            return True
                
        return [iS for iS in range(S - W * L + 1) if concatStartsAt(iS)]