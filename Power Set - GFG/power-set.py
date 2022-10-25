#User function Template for python3
def genStr(res, s, t, i):
    if i >= len(s):
        return
    res.append(t+s[i])
    genStr(res, s, t+s[i], i+1)
    genStr(res, s, t, i+1)


class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		res = []
		genStr(res, s, "", 0)
		return sorted(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends