#User function Template for python3
def isGood(n, D):
    d = n%10
    if d == D:
        return False
    n //= 10
    s = d
    while n:
        d = n%10
        if d == D or d <= s:
            return False
        s += d
        n //= 10
    return True


class Solution:
    def goodNumbers(self,L,R,D):
        #code here
        ret = []
        for i in range(L, R+1):
            if isGood(i, D):
                ret.append(i)
        return ret



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        L,R,D=map(int,input().strip().split())
        ob=Solution()
        ans=ob.goodNumbers(L,R,D)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends