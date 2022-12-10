#User function Template for python3

class Solution:
    def minimizeCost(self, height, n, k):
        if not height:
            return 0
            
        ret = [float('inf')]*n
        ret[0] = 0
        
        for i in range(n):
            for j in range(i-k, i):
                if j >= 0:
                    d = abs(height[i]-height[j])
                    ret[i] = min(ret[i], d+ret[j])
        
        return ret[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimizeCost(height, n, k))
# } Driver Code Ends