#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        n = len(txt)
        m = len(pat)
        
        pi = [0]*m
        i, j = 0, 1
        
        while i < m and j < m:
            if pat[j] == pat[i]:
                pi[j] = i+1
                i += 1
            else:
                i = 0
            j += 1
            
        i = 0  # index for txt[]
        j = 0
        ret = []
        while (n - i) >= (m - j):
            if pat[j] == txt[i]:
                i += 1
                j += 1
     
            if j == m:
                ret.append(i-j+1)
                j = pi[j-1]
     
            # mismatch after j matches
            elif i < n and pat[j] != txt[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = pi[j-1]
                else:
                    i += 1
        return ret
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends