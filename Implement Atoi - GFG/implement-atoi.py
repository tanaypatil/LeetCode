#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here
        neg = False
        if string[0] == "-":
            neg = True
            string = string[1:]
        n = len(string)
        s = 0
        for i in range(n-1, -1, -1):
            if not string[i].isnumeric():
                return -1
            s += int(string[i]) * (10**(n-1-i))
        return -s if neg else s


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends