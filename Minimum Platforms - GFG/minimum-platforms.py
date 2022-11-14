#User function Template for python3
class Times:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        times = []
        
        platforms, ret = 0, 0
        
        for i in range(n):
            times.append((arr[i], 'a'))
            times.append((dep[i], 'd'))
            
        times.sort(key=lambda x: (x[0], x[1]))
        
        for i in range(len(times)):
            t, p = times[i]
            
            if p == 'a':
                platforms += 1
            else:
                platforms -= 1
            
            ret = max(ret, platforms)
            
        return ret
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends