from collections import Counter


class Solution:
    def equalFreq(self, freq1, freq2):
        if freq1.keys() == freq2.keys():
            for k, v in freq1.items():
                if v < freq2[k]:
                    return False
            return True
        else: return False
    
    def minWindow(self, s: str, t: str) -> str:
        countsT = Counter(t)
        countsTSum = sum(countsT.values())
        countsTKeys = countsT.keys()
        countsS = Counter()
        
        left = 0
        res = 99999999
        ret = ""
        for right, c in enumerate(s):
            if countsT[c]:
                countsS[c] += 1
            
            while self.equalFreq(countsS, countsT):
                if right-left+1 <= res:
                    res = right-left+1
                    ret = s[left: right+1]
                if countsS[s[left]]:
                    countsS[s[left]] -= 1
                if countsS[s[left]] == 0:
                    del countsS[s[left]]
                left += 1
        return ret