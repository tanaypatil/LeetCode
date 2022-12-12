#User function Template for python3
def chkSum(arr, target_sum, current_sum, index, res):
    if index >= len(arr):
        return
    if (current_sum + arr[index])%(10**9+7) == target_sum:
        res[0] = (res[0] + 1)%(10**9+7)
    if (current_sum + arr[index])%(10**9+7) <= target_sum:
        chkSum(arr, target_sum, current_sum+arr[index], index+1, res)
    if current_sum <= target_sum:
        chkSum(arr, target_sum, current_sum, index+1, res)

class Solution:
	def perfectSum(self, arr, n, s):
		prev = [0]*(s+1)
        prev[0] = 1
        
        MOD = 10**9+7
        
        for i in range(n):
            dp = [0]*(s+1)
            dp[0] = 1
            for j in range(s+1):
                not_taken = prev[j]
                taken = 0
                if arr[i] <= j:
                    taken = prev[j-arr[i]]
                dp[j] = (taken%MOD + not_taken%MOD)%MOD
                    
            prev = dp
            
        return prev[-1]
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends