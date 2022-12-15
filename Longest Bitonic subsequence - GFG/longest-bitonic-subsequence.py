#User function Template for python3

class Solution:
	def LongestBitonicSequence(self, nums):
		# Code here
		n = len(nums)
		inc = [1]*n
		dec = [1]*n
		
		for i in range(1, n):
		    for j in range(i):
		        if nums[i] > nums[j] and inc[i] < inc[j] + 1:
		            inc[i] = inc[j]+1

		for i in range(n-2, -1, -1):
		    for j in range(i+1, n):
		        if nums[i] > nums[j] and dec[i] < dec[j] + 1:
		            dec[i] = dec[j] + 1
        
        m = 1        
        for i in range(n):
            m = max(m, inc[i] + dec[i] - 1)
        return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends