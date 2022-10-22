#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        if R == 0:
            return 1
        s = Solution()
        N = N%(10**9+7)
        if R%2:
            return (N*(s.power(N*N, (R-1)//2))%(10**9+7))%(10**9+7)
        else:
            return s.power(N*N, R//2)%(10**9+7)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends