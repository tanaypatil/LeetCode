#User function Template for python3
from collections import defaultdict
import math
class Solution:
    def dfs(self, index, x, N):
        if index >= N:
            if x == Solution.target:
                return 1
            return 0
        if (index, x) in Solution.mem:
            return Solution.mem[(index, x)]
                
        a = self.dfs(index+1, x^Solution.arr[index], N)
        b = self.dfs(index+1, x, N)
            
        Solution.mem[(index, x)] = a+b
        return a+b
        
    def subsetXOR(self, arr, N, target): 
        # code here
        Solution.arr = arr
        Solution.mem = {}
        Solution.target = target
        return self.dfs(0, 0, N)


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = input().split()
        N = int(N)
        K = int(K)
        arr = input().split(' ')
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        print(ob.subsetXOR(arr,N,K))
# } Driver Code Ends