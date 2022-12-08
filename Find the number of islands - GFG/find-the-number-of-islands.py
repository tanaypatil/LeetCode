#User function Template for python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, r, c):
        if Solution.visited[(r, c)]:
            return
        Solution.visited[(r, c)] = True
        
        x = [-1, 0, 1, -1, 1, -1, 0, 1]
        y = [-1, -1, -1, 0, 0, 1, 1, 1]
        
        for i in range(8):
            a = r+x[i]
            b = c+y[i]
            if 0 <= a < Solution.n and 0 <= b < Solution.m and not Solution.visited[(a, b)] and Solution.grid[a][b]:
                self.dfs(a, b)
    
    
    def numIslands(self,grid):
        #code here
        Solution.visited = defaultdict(bool)
        n = len(grid)
        m = len(grid[0])
        Solution.n = n
        Solution.m = m
        Solution.grid = grid
        ans = 0
        for i in range(n):
            for j in range(m):
                if not Solution.visited[(i, j)] and grid[i][j]:
                    # print(i, j)
                    ans += 1
                    self.dfs(i, j)
        return ans
                    
                    
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends