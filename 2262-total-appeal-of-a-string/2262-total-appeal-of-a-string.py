class Solution:
    def appealSum(self, s: str) -> int:
        
        def noSubstringsWithAtLeastOneCh(ch):
            res = 0 # number of substrings without even one ch
            count = 0
            
            for c in s:
                if c == ch:
                    res += (count*(count+1)) // 2
                    count = 0
                else:
                    count += 1
            
            res += (count*(count+1)) // 2
            return self.total_substrings - res
        
        n = len(s)
        self.total_substrings = (n * (n+1)) // 2
        ans = 0
        for i in range(ord("a"), ord("z")+1):
            ans += noSubstringsWithAtLeastOneCh(chr(i))
        return ans
        
            
            