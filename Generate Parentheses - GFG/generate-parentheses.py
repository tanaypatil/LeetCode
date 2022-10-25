#User function Template for python3
def genPar(stack, res, s, n, oc):
    if len(s) >= n:
        if not stack:
            res.append(s)
        return
    if oc < n//2:
        genPar(stack+["("], res, s+"(", n, oc+1)
    if stack:
        stack.pop()
        genPar(stack, res, s+")", n, oc)

class Solution:
    def AllParenthesis(self,n):
        #code here
        ret = []
        genPar([], ret, "", 2*n, 0)
        return ret


#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends