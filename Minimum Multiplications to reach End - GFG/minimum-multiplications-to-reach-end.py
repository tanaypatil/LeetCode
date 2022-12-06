#User function Template for python3

from typing import List
from collections import deque, defaultdict
from heapq import heappush, heappop

 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        if start == end:
            return 0
        if not arr:
            return -1
            
        arr = list(set(arr))
        
        adj = defaultdict(list)
        
        MOD = 10**5
        dist = [float('inf')]*100000
                    
        q = deque({(0, start)})
        
        while q:
            steps, num = q.popleft()
            num = num%MOD
            if num == end:
                return steps
            
            for a in arr:
                p = (a*num)%MOD
                if dist[p] > 1+steps:
                    dist[p] = 1+steps
                    q.append((dist[p], p))
                    
        return -1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends