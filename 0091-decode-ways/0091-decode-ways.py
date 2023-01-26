class Solution:
    def numDecodings(self, s: str) -> int:
        def find(i):
            if i == len(s):
                return 1
            
            if i in mem:
                return mem[i]
            
            cs = 0
            
            if s[i] == "0":
                return cs
            
            cs += find(i+1)
            
            if s[i] == "1" and i+1 < len(s):
                cs += find(i+2)
                
            if s[i] == "2" and i+1 < len(s) and int(s[i+1]) <= 6:
                cs += find(i+2)
                
            mem[i] = cs
            return cs
        mem = {}
        return find(0)