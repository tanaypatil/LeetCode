class Solution:
    wl = {}
    visited = {}
    end_word = ""
    jumps = 0
    def jump(self, s, c):
        if s == Solution.end_word:
            Solution.jumps = min(Solution.jumps, c)
            return
        if Solution.visited[s] < c:
            return
        Solution.visited[s] = min(Solution.visited[s], c)
        for i in range(len(s)):
            for j in range(26):
                cs = s[:i] + chr(97+j) + s[i+1:]
                if Solution.wl[cs]:
                    if Solution.visited[cs] > c+1:
                        self.jump(cs, c+1)
    
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         Solution.wl = defaultdict(bool)
#         Solution.end_word = endWord
#         Solution.visited = defaultdict(int)
#         Solution.jumps = float('inf')
        
#         found = 0
#         for word in wordList:
#             Solution.visited[word] = float('inf')
#             Solution.wl[word] = True
#             if word == endWord:
#                 found = 1
                
#         if not found:
#             return 0
#         Solution.visited[beginWord] = 1
#         self.jump(beginWord, 1)
        
#         if Solution.jumps == float('inf'):
#             return 0
        
#         return Solution.jumps
        q = deque({(beginWord, 0)})
        mem = defaultdict(int)
        wl = set(wordList)
        while q:
            word, count = q.popleft()
            mem[word] = count
            if word == endWord:
                return count+1
            for i in range(len(word)):
                for j in range(26):
                    cs = word[:i] + chr(97+j) + word[i+1:]
                    if cs in wl and cs != beginWord:
                        # print(cs)
                        wl.remove(cs)
                        q.append((cs, count+1))
                        
        
        return 0