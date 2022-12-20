class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,string):
        # Code here
        n = len(string)
        mat = [[0]*n for _ in range(n)]
        
        for i in range(n):
            mat[i][i] = 1
            
        MOD = 10**9+7
            
        for l in range(2, n+1):
            for i in range(n):
                j = i+l-1
                if j < n:
                    if string[i] == string[j]:
                        mat[i][j] = (1 + mat[i+1][j] + mat[i][j-1])%MOD
                    else:
                        mat[i][j] = ((mat[i+1][j]%MOD + mat[i][j-1]%MOD)%MOD - mat[i+1][j-1])%MOD
        return mat[0][-1]



#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPS(input().strip()))

# } Driver Code Ends