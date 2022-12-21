#User function Template for python3
from collections import defaultdict


class Solution:
    def atMostK (self,s, k):
        if k < 0:
            return 0
            
        i = 0
        j = 0
        cnt = 0
        res = 0
        m = [0 for i in range (26)]
        
        while j < len (s):
            m[ord (s[j]) - ord ('a')] += 1
            if m[ord (s[j]) - ord ('a')] == 1:
                cnt += 1
            
            while cnt > k:
                m[ord (s[i]) - ord ('a')] -= 1
                if m[ord (s[i]) - ord ('a')] == 0:
                    cnt -= 1
                i += 1
            
            res += j - i + 1
            j += 1
        return res
    
    def substrCount (self,s, k):
        return self.atMostK (s, k) - self.atMostK (s, k-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends