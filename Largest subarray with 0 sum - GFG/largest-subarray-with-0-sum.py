#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        sums = {}
        s = 0
        m = 0
        for i, a in enumerate(arr):
            s += a
            if not s:
                m = i+1
            else:
                if s in sums:
                    m = max(m, i-sums[s])
                else:
                    sums[s] = i
        return m

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends