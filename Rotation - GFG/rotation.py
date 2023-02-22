#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        l, h = 0, len(arr)-1
        while l <= h:
            m = l + (h-l)//2
            prev = (m-1+n)%n
            nex = (m+1)%n
            if arr[m] < arr[prev] and arr[m] <= arr[nex]:
                return m
            if arr[m] < arr[h]:
                h = m-1
            else:
                l = m+1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends