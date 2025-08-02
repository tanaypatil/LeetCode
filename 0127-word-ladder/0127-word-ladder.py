class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        counts = Counter(wordList)
        
        if not counts[endWord]:
            return 0

        q = deque({beginWord})
        counts[beginWord] -= 1

        def move(word):
            for i in range(len(word)):
                for j in range(26):
                    if chr(j + ord('a')) != word[i]:
                        next_word = word[:i] + chr(j + ord('a')) + word[i+1:]
                        if counts[next_word]:
                            yield next_word

        dist = 0
        while q:
            s = len(q)
            dist += 1
            for _ in range(s):
                word = q.popleft()
                if word == endWord:
                    return dist
                for next_word in move(word):
                    q.append(next_word)
                    counts[next_word] -= 1
        
        return 0