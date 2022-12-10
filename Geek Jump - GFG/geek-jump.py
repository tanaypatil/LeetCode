#User function Template for python3
from collections import defaultdict


class Solution:
    def dfs(self, i, d, n):
        if Solution.visited[(i, d)]:
            return
        Solution.visited[(i, d)] = True
        if i == n-1:
            Solution.ret = min(Solution.ret, d)
            return
        if i+1 < n:
            self.dfs(i+1, d+abs(Solution.height[i]-Solution.height[i+1]), n)
        if i+2 < n:
            self.dfs(i+2, d+abs(Solution.height[i]-Solution.height[i+2]), n)
            

    def minimumEnergy(self, height, n):
        # Code here
        # if not height:
        #     return 0
            
        # Solution.height = height
        # Solution.ret = float('inf')
        # Solution.visited = defaultdict(bool)
        
        # self.dfs(0, 0, n)
        
        # return Solution.ret if Solution.ret != float('inf') else -1
        
        ret = [0]*n
        for i in range(1, n):
            if i-1 >= 0:
                d = abs(height[i]-height[i-1])
                ret[i] = min(ret[i-1]+d, ret[i]) if ret[i] != 0 else ret[i-1]+d
                
            if i-2 >= 0:
                d = abs(height[i]-height[i-2])
                ret[i] = min(ret[i-2]+d, ret[i]) if ret[i] != 0 else ret[i-2]+d
                
        return ret[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends