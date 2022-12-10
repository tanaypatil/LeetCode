#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		if not arr:
		    return -1
		    
		v1 = arr[0]
		
		if n == 1:
		    return v1
		    
		v2 = max(v1, arr[1])
		if n == 2:
		    return v2
		    
		    
		ret = [float('inf')]*n
		ret[0], ret[1] = v1, v2
		for i in range(2, n):
		    ret[i] = max(arr[i]+ret[i-2], ret[i-1])
        return ret[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends