#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        if n == 1:
            return a[0]
        # code here
        sol = [0]*n
        sol[0], sol[1] = a[0], max(a[0], a[1])
        
        for i in range(2, n):
            sol[i] = max(sol[i-1], a[i] + sol[i-2], )
        
        return max(sol[-1], sol[-2])


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends